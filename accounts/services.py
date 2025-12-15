from django.db import IntegrityError
from django.db.models import Q

from accounts.models import UserRole
from accounts.graphql.types import UserRoleType, CreateUserRoleResponse, GetUserRoleResponse


class UserRoleService:

    @staticmethod
    def create_role(input):
        try:
            role = UserRole.objects.create(
                name=input.name,
                description=input.description
            )

            return CreateUserRoleResponse(
                id=role.id_user_role,
                status_code=200,
                message="Rol creado con éxito",
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
            return CreateUserRoleResponse(
                id=None,
                status_code=400,
                message="Error al crear rol",
                data=None,
                error="El nombre del rol ya existe"
            )

        except Exception as e:
            return CreateUserRoleResponse(
                id=None,
                status_code=500,
                message="Error interno del servidor",
                data=None,
                error=str(e)
            )

    def get_roles(input):
        """
        Busca roles filtrando opcionalmente por id_user_role o name.
        Si no se pasa ningún filtro, devuelve todos los roles.
        """
        try:
            # Construir filtros opcionales
            filters = {}
            if input:
                if input.id is not None:
                    filters['id_user_role'] = input.id
                if input.name is not None:
                    filters['name'] = input.name

            # Obtener roles filtrados o todos si no hay filtros
            roles_qs = UserRole.objects.filter(
                **filters) if filters else UserRole.objects.all()

            if not roles_qs.exists():
                return GetUserRoleResponse(
                    id=None,
                    status_code=404,
                    message="No se encontraron roles",
                    data=[],
                    error="No hay registros con esos filtros"
                )

            # Mapear queryset a lista de UserRoleType
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

            return GetUserRoleResponse(
                id=None,
                status_code=200,
                message=f"{len(roles_list)} roles encontrados",
                data=roles_list,
                error=None
            )

        except Exception as e:
            return GetUserRoleResponse(
                id=None,
                status_code=500,
                message="Error interno del servidor",
                data=None,
                error=str(e)
            )
