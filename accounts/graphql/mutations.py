import strawberry
from strawberry.types import Info

from accounts.services import UserRoleService
from accounts.graphql.inputs import CreateUserRoleInput
from accounts.graphql.types import CreateUserRoleResponse
from graph_ql.utils import log_graphql_request


@strawberry.type(
    description="Mutations relacionadas con roles de usuario."
)
class UserRoleMutation:

    @strawberry.mutation(
        description="Crea un nuevo rol de usuario"
    )
    def create_user_role(self, info: Info, input: CreateUserRoleInput) -> CreateUserRoleResponse:

        # Crear log
        # logs = log_graphql_request(info.context["request"], info)

        return UserRoleService.create_role(input)
