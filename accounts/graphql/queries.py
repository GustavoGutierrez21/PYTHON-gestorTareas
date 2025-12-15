import strawberry
from typing import Optional, List
from uuid import UUID
from accounts.graphql.types import GetUserRoleResponse
from accounts.services import UserRoleService
from accounts.graphql.inputs import GetUserRoleInput


@strawberry.type(
    description="Queries relacionadas con roles de usuario"
)
class UserRoleQuery:

    @strawberry.field(
        description="Obtiene todos los roles de usuario, opcionalmente filtrando por ID o nombre."
    )
    def get_user_roles(
        self,
        input: Optional[GetUserRoleInput] = None
    ) -> GetUserRoleResponse:

        return UserRoleService.get_roles(input)
