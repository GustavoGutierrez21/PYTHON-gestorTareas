from django.db import IntegrityError

from accounts.models import UserRole
from accounts.graphql.types import UserRoleType, UserRoleResponse


class UserRoleService:

    @staticmethod
    def create_role(name: str, description: str | None):
        try:
            role = UserRole.objects.create(
                name=name,
                description=description
            )

            return UserRoleResponse(
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
            return UserRoleResponse(
                id=None,
                status_code=400,
                message="Error al crear rol",
                data=None,
                error="El nombre del rol ya existe"
            )

        except Exception as e:
            return UserRoleResponse(
                id=None,
                status_code=500,
                message="Error interno del servidor",
                data=None,
                error=str(e)
            )
