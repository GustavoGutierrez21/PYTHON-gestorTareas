from django.db import IntegrityError, transaction
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from typing import Optional

from accounts.models import User, UserRole
from core.logging.logger import Logger
from accounts.graphql.inputs import CreateUserInput, CreateUserRoleInput, DeleteUserRoleInput, GetUserRolesInput, UpdateUserRoleInput
from accounts.graphql.types import CreateUserResponse, DeleteUserRoleResponse, UpdateUserRoleResponse, UserRoleType, CreateUserRoleResponse, GetUserRoleResponse, UserType


# ===============================================================================================================================================================================
# region ROLES
# ===============================================================================================================================================================================
class UserRoleService:
    logger = Logger("Roles")

    # ===================================
    # region create rol
    # ===================================
    def create_role(
        self,
        input: CreateUserRoleInput,
    ) -> CreateUserRoleResponse:
        try:
            # Crear rol
            role = UserRole.objects.create(
                name=input.name,
                description=input.description
            )

            # Respuesta
            self.logger.log(f"Rol creado con éxito. {role}")
            
            return CreateUserRoleResponse(
                id=None,
                status_code=201,
                message="Rol creado con éxito.",
                data=UserRoleType(
                    id_user_role=role.id_user_role,
                    name=role.name,
                    description=role.description,
                    created_at=role.created_at,
                    updated_at=role.updated_at,
                    user_create=role.user_create,
                    user_update=role.user_update
                ),
                error=None
            )

        except IntegrityError:
            self.logger.warn(f'El nombre del rol ya existe. {input.name}')
            
            return CreateUserRoleResponse(
                id=None,
                status_code=400,
                message="Error al crear rol.",
                data=None,
                error="El nombre del rol ya existe."
            )

        except Exception as e:
            self.logger.error(f'Error al crear rol. {e}')

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
    def get_roles(
        self,
        input: Optional[GetUserRolesInput] = None
    ) -> GetUserRoleResponse:
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
                self.logger.warn(f"No se encontraron roles con los filtros {filters}")
                
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
                    updated_at=role.updated_at,
                    user_create=role.user_create,
                    user_update=role.user_update
                )
                for role in roles_qs
            ]

            # Respuesta
            self.logger.log(f"Roles encontrados con éxito. {roles_list}")

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
            self.logger.error(f"Error al obtener roles. {e}")

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
    def update_role(
        self,
        input: UpdateUserRoleInput
    ) -> UpdateUserRoleResponse:
        try:
            # Verificar si el rol existe
            role = UserRole.objects.filter(
                id_user_role=input.id_user_role
            ).first()

            if not role:
                self.logger.warn(f"Rol no encontrado con el id. {input.id_user_role}")
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
            self.logger.log(f"Rol actualizado con éxito. {role}")
            
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
                    user_create=role.user_create,
                    user_update=role.user_update
                ),
                error=None
            )

        except IntegrityError:
            self.logger.warn(f'El nombre del rol ya existe. {input.name}')
            
            return UpdateUserRoleResponse(
                id=None,
                status_code=400,
                message="Error al actualizar rol.",
                data=None,
                error="El nombre del rol ya existe."
            )

        except Exception as e:
            self.logger.error(f'Error al actualizar rol. {e}')

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
    def delete_role(
        self,
        input: DeleteUserRoleInput
    ) -> DeleteUserRoleResponse:
        try:
            # Verificar si el rol existe
            role = UserRole.objects.filter(
                id_user_role=input.id_user_role
            ).first()

            # Rol no existe
            if not role:
                self.logger.warn(f"Rol no encontrado con el id. {input.id_user_role}")
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
            self.logger.log(f"Rol eliminado con éxito. {role_id}")
            
            return DeleteUserRoleResponse(
                id=None,
                status_code=200,
                message="Rol eliminado con éxito",
                error=None
            )

        except Exception as e:
            self.logger.error(f"Error al eliminar rol. {e}")
            
            return DeleteUserRoleResponse(
                id=None,
                status_code=500,
                message="Error interno del servidor",
                error=str(e)
            )
    # endregion


# ===============================================================================================================================================================================
# region USERS
# ===============================================================================================================================================================================
class UserService:
    logger = Logger("Users")
    
    
    # ===================================
    # region create rol
    # ===================================
    def create_user(
        self,
        input: CreateUserInput,
    ) -> CreateUserResponse:
        try:
            # Validar email
            try:
                validate_email(input.email)
                
            except ValidationError:
                self.logger.warn(f"Email inválido: {input.email}")
                
                return CreateUserResponse(
                    id=None,
                    status_code=400,
                    message="Email inválido",
                    data=None,
                    error="El correo electrónico no tiene un formato válido.",
                )


            # Validar password segura
            try:
                validate_password(input.password)
            except ValidationError as e:
                self.logger.warn(f"Contraseña insegura: {input.password}")
                
                return CreateUserResponse(
                    id=None,
                    status_code=400,
                    message="Contraseña insegura.",
                    data=None,
                    error="La contraseña no cumple con lo mínimo requerido",
                )


            # Verificar email único
            if User.objects.filter(email=input.email).exists():
                self.logger.warn(f"Email ya registrado: {input.email}")
                
                return CreateUserResponse(
                    id=None,
                    status_code=409,
                    message="Correo ya registrado",
                    data=None,
                    error="Ya existe un usuario con este correo",
                )


            # Verificar rol existente
            try:
                role = UserRole.objects.get(id_user_role=input.id_user_role)
                
            except UserRole.DoesNotExist:
                self.logger.warn(f"Rol no encontrado: {input.id_user_role}")
                
                return CreateUserResponse(
                    id=None,
                    status_code=404,
                    message="Rol no encontrado",
                    data=None,
                    error="El rol especificado no existe",
                )


            # Flags según rol
            is_admin = role.name == "ADMIN"


            # Crear usuario (transacción)
            with transaction.atomic():
                user = User.objects.create(
                    id_user_role=role,
                    name=input.name,
                    last_name=input.last_name,
                    username=input.username,
                    email=input.email,
                    status=input.status.value,
                    is_staff=is_admin,
                    is_superuser=is_admin,
                )
                user.set_password(input.password)
                user.save()




            # Respuesta OK
            self.logger.log(f"Usuario creado con éxito. {user}")
            
            return CreateUserResponse(
                id=None,
                status_code=201,
                message="Usuario creado correctamente",
                data=UserType(
                    id_user=user.id_user,
                    id_user_role=role.id_user_role,
                    name=user.name,
                    last_name=user.last_name,
                    username=user.username,
                    email=user.email,
                    status=input.status,
                    last_login=user.last_login,
                    created_at=user.created_at,
                    updated_at=user.updated_at,
                ),
                error=None,
            )

        except IntegrityError as e:
            
            self.logger.error(f'Error de base de datos: {e}')
            return CreateUserResponse(
                id=None,
                status_code=500,
                message="Error de base de datos",
                data=None,
                error="No se pudo crear el usuario",
            )

        except Exception as e:
            self.logger.error(f'Error interno: {e}')
            return CreateUserResponse(
                id=None,
                status_code=500,
                message="Error interno",
                data=None,
                error='Error interno del servidor.',
            )
    # endregion