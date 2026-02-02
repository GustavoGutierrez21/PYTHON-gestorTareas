import strawberry

from core.logging.logger import Logger
from accounts.services import UserRoleService
from accounts.graphql.inputs import CreateUserRoleInput, DeleteUserRoleInput, UpdateUserRoleInput
from accounts.graphql.types import CreateUserRoleResponse, DeleteUserRoleResponse, UpdateUserRoleResponse

logger = Logger("Roles")


@strawberry.type(
    description="Mutations relacionadas con roles de usuario."
)
class UserRoleMutation:
    # ============================
    # region crear rol
    # ============================
    @strawberry.mutation(
        description="Crea un nuevo rol de usuario."
    )
    def create_user_role(
        self,
        input: CreateUserRoleInput
    ) -> CreateUserRoleResponse:
        logger.log(f"Creando rol con los siguientes parametros {input}")
        return UserRoleService.create_role(input)
    # endregion
    
    
    # ============================
    # region update rol
    # ============================
    @strawberry.mutation(
        description="Actualizar un rol de usuario."
    )
    def update_user_role(
        self,
        input: UpdateUserRoleInput
    ) -> UpdateUserRoleResponse:
        logger.log(f"Actualizando rol con los siguientes parametros {input}")
        return UserRoleService.update_role(input)
    
    
    # ============================
    # region delete rol
    # ============================
    @strawberry.mutation(
        description="Elimina un rol de usuario."
    )
    def delete_user_role(
        self,
        input: DeleteUserRoleInput
    ) -> DeleteUserRoleResponse:
        logger.log(f"Eliminando rol con los siguientes parametros {input}")
        return UserRoleService.delete_role(input)
    # endregion