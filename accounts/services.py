from django.db import IntegrityError

from typing import Optional

from accounts.models import UserRole
from core.logging.logger import Logger
from accounts.graphql.inputs import CreateUserRoleInput, DeleteUserRoleInput, GetUserRolesInput, UpdateUserRoleInput
from accounts.graphql.types import DeleteUserRoleResponse, UpdateUserRoleResponse, UserRoleType, CreateUserRoleResponse, GetUserRoleResponse

logger = Logger("Roles")


class UserRoleService:

    # ===================================
    # region create rol
    # ===================================
    @staticmethod
    def create_role(input: CreateUserRoleInput):
        try:
            # Crear rol
            role = UserRole.objects.create(
                name=input.name,
                description=input.description
            )

            # Respuesta
            logger.log(f"Rol creado con éxito. {role}")
            
            return CreateUserRoleResponse(
                id=None,
                status_code=200,
                message="Rol creado con éxito.",
                data=UserRoleType(
                    id_user_role=role.id_user_role,
                    name=role.name,
                    description=role.description,
                    created_at=role.created_at,
                    updated_at=role.updated_at,
                ),
                error=None
            )

        except IntegrityError:
            logger.warn(f'El nombre del rol ya existe. {input.name}')
            
            return CreateUserRoleResponse(
                id=None,
                status_code=400,
                message="Error al crear rol.",
                data=None,
                error="El nombre del rol ya existe."
            )

        except Exception as e:
            logger.error(f'Error al crear rol. {e}')

            return CreateUserRoleResponse(
                id=None,
                status_code=500,
                message="Error interno del servidor.",
                data=None,
                error='Error interno al crear rol.'
            )
    # endregion

    # ===================================
    # region see roles
    # ===================================

    @staticmethod
    def get_roles(input: Optional[GetUserRolesInput] = None):
        try:
            # Defaults
            page = 1
            limit = 10
            filters = {}

            # Aplicar filtros y paginación
            if input:
                # Filtros
                if input.filters:
                    if input.filters.id is not None:
                        filters['id_user_role'] = input.filters.id
                    if input.filters.name is not None:
                        filters['name__icontains'] = input.filters.name

                # Paginación
                if input.pagination:
                    page = max(input.pagination.page, 1)
                    limit = max(input.pagination.limit, 1)

            # Cálculo de offset
            offset = (page - 1) * limit

            # Obtener roles
            roles_qs = (
                UserRole.objects
                .filter(**filters)
                .order_by('-created_at')
            )

            # Calcular total de roles
            total_roles = roles_qs.count()

            if total_roles == 0:
                logger.warn(f"No se encontraron roles con los filtros {filters}")
                
                return GetUserRoleResponse(
                    id=None,
                    status_code=404,
                    message="No se encontraron roles",
                    total=total_roles,
                    page=page,
                    limit=limit,
                    data=[],
                    error="No hay registros con esos filtros"
                )

            # Aplicar paginación
            roles_qs = roles_qs[offset: offset + limit]

            # Crear lista de roles
            roles_list = [
                UserRoleType(
                    id_user_role=role.id_user_role,
                    name=role.name,
                    description=role.description,
                    created_at=role.created_at,
                    updated_at=role.updated_at
                )
                for role in roles_qs
            ]

            # Respuesta
            logger.log(f"Roles encontrados con éxito. {roles_list}")

            return GetUserRoleResponse(
                id=None,
                status_code=200,
                message='Roles encontrados con éxito.',
                total=total_roles,
                page=page,
                limit=limit,
                data=roles_list,
                error=None
            )

        except Exception as e:
            logger.error(f"Error al obtener roles. {e}")

            return GetUserRoleResponse(
                id=None,
                status_code=500,
                total=None,
                page=None,
                limit=None,
                message="Error interno del servidor",
                data=None,
                error='Error interno al obtener roles.'
            )
    # endregion


    # ===================================
    # region update rol
    # ===================================
    @staticmethod
    def update_role(input: UpdateUserRoleInput):
        try:
            # Verificar si el rol existe
            role = UserRole.objects.filter(
                id_user_role=input.id_user_role
            ).first()

            if not role:
                logger.warn(f"Rol no encontrado con el id. {input.id_user_role}")
                return UpdateUserRoleResponse(
                    id=None,
                    status_code=404,
                    message="Rol no encontrado.",
                    data=None,
                    error="No existe un rol con ese ID."
                )

            # Actualizar solo campos enviados
            if input.name is not None:
                role.name = input.name
            if input.description is not None:
                role.description = input.description

            # Guardar cambios
            role.save()

            # Respuesta
            logger.log(f"Rol actualizado con éxito. {role}")
            
            return UpdateUserRoleResponse(
                id=None,
                status_code=200,
                message="Rol actualizado con éxito.",
                data=UserRoleType(
                    id_user_role=role.id_user_role,
                    name=role.name,
                    description=role.description,
                    created_at=role.created_at,
                    updated_at=role.updated_at,
                ),
                error=None
            )

        except IntegrityError:
            logger.warn(f'El nombre del rol ya existe. {input.name}')
            
            return UpdateUserRoleResponse(
                id=None,
                status_code=400,
                message="Error al actualizar rol.",
                data=None,
                error="El nombre del rol ya existe."
            )

        except Exception as e:
            logger.error(f'Error al actualizar rol. {e}')

            return UpdateUserRoleResponse(
                id=None,
                status_code=500,
                message="Error interno del servidor.",
                data=None,
                error=str(e)
            )
    # endregion

    # ===================================
    # region delete role
    # ===================================

    @staticmethod
    def delete_role(input: DeleteUserRoleInput):
        try:
            # Verificar si el rol existe
            role = UserRole.objects.filter(
                id_user_role=input.id_user_role
            ).first()

            # Rol no existe
            if not role:
                logger.warn(f"Rol no encontrado con el id. {input.id_user_role}")
                return DeleteUserRoleResponse(
                    id=None,
                    status_code=404,
                    message="Rol no encontrado",
                    error="No existe un rol con ese ID"
                )

            # Eliminar rol
            role_id = role.id_user_role
            role.delete()

            # Respuesta
            logger.log(f"Rol eliminado con éxito. {role_id}")
            
            return DeleteUserRoleResponse(
                id=None,
                status_code=200,
                message="Rol eliminado con éxito",
                error=None
            )

        except Exception as e:
            logger.error(f"Error al eliminar rol. {e}")
            
            return DeleteUserRoleResponse(
                id=None,
                status_code=500,
                message="Error interno del servidor",
                error=str(e)
            )
    # endregion
