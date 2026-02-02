import strawberry
from typing import Optional

from core.logging.logger import Logger
from accounts.services import UserRoleService
from accounts.graphql.inputs import GetUserRolesInput
from accounts.graphql.types import GetUserRoleResponse

logger = Logger("Roles")


@strawberry.type(
    description="Queries relacionadas con roles de usuario"
)
class UserRoleQuery:

    @strawberry.field(
        description="Obtiene todos los roles de usuario, opcionalmente filtrando por ID o nombre."
    )
    def get_user_roles(
        self,
        input: Optional[GetUserRolesInput] = None
    ) -> GetUserRoleResponse:
        logger.log(f"Buscando roles con los siguientes parametros {input}")
        return UserRoleService.get_roles(input)
