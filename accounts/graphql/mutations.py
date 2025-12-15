import strawberry

from accounts.services import UserRoleService
from accounts.graphql.inputs import CreateUserRoleInput
from accounts.graphql.types import UserRoleType, UserRoleResponse


@strawberry.type(
    description="Mutations relacionadas con roles de usuario."
)
class UserRoleMutation:

    @strawberry.mutation(
        description="Crea un nuevo rol de usuario"
    )
    def create_user_role(self, input: CreateUserRoleInput) -> UserRoleResponse:
        return UserRoleService.create_role(
            name=input.name,
            description=input.description
        )
