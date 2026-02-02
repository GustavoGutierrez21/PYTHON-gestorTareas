import strawberry
from strawberry.types import Info

from core.logging.logger import Logger
from accounts.services import UserRoleService, UserService
from accounts.graphql.inputs import CreateUserInput, CreateUserRoleInput, DeleteUserRoleInput, UpdateUserRoleInput
from accounts.graphql.types import CreateUserResponse, CreateUserRoleResponse, DeleteUserRoleResponse, UpdateUserRoleResponse


# ===============================================================================================================================================================================
# region ROLES
# ===============================================================================================================================================================================
@strawberry.type(
    description="Mutations relacionadas con roles de usuario."
)
class UserRoleMutation:
    logger = Logger("Roles")
    service = UserRoleService()


    # ============================
    # region crear rol
    # ============================
    @strawberry.mutation(
        description="Crea un nuevo rol de usuario."
    )
    @staticmethod
    def create_user_role(input: CreateUserRoleInput) -> CreateUserRoleResponse:
        UserRoleMutation.logger.log(f"Creando rol con los siguientes parametros {input}")
        return UserRoleMutation.service.create_role(input)
    # endregion
    
    
    # ============================
    # region update rol
    # ============================
    @strawberry.mutation(
        description="Actualizar un rol de usuario."
    )
    @staticmethod
    def update_user_role(input: UpdateUserRoleInput) -> UpdateUserRoleResponse:
        UserRoleMutation.logger.log(f"Actualizando rol con los siguientes parametros {input}")
        return UserRoleMutation.service.update_role(input)
    
    
    # ============================
    # region delete rol
    # ============================
    @strawberry.mutation(
        description="Elimina un rol de usuario."
    )
    @staticmethod
    def delete_user_role(input: DeleteUserRoleInput) -> DeleteUserRoleResponse:
        UserRoleMutation.logger.log(f"Eliminando rol con los siguientes parametros {input}")
        return UserRoleMutation.service.delete_role(input)
    # endregion


# ===============================================================================================================================================================================
# region USER
# ===============================================================================================================================================================================
@strawberry.type(
    description="Mutations relacionadas con usuarios."
)
class UsersMutation:
    logger = Logger("Users")
    service = UserService()

    # ============================
    # region crear usuario
    # ============================
    @strawberry.mutation(
        description="Crea un nuevo usuario."
    )
    @staticmethod
    def create_user(input: CreateUserInput) -> CreateUserResponse:
        UsersMutation.logger.log(
            f"Creando usuario con los siguientes parametros {input}"
        )
        return UsersMutation.service.create_user(input)
    # endregion