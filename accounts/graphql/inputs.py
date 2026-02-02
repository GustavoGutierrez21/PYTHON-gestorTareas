import strawberry
from enum import Enum
from uuid import UUID
from typing import Optional

from core.graphql.inputs.pagination import PaginationInput

# ===============================================================================================================================================================================
# region ROLES
# ===============================================================================================================================================================================



# ===================================
# region create rol Input
# ===================================
@strawberry.input(
    description="Datos necesarios para crear un rol de usuario."
)
class CreateUserRoleInput:
    name: str = strawberry.field(
        description="Nombre único del rol."
    )
    
    description: str = strawberry.field(
        description="Descripción del rol."
    )
# endregion


# ===================================
# region see roles Input
# ===================================
@strawberry.input(
    description="Datos con los que puedes filtrar al buscar roles."
)
class UserRoleFiltersInput:
    id: Optional[UUID] = strawberry.field(
        description="Id del rol a buscar.",
        default=None,
    )

    name: Optional[str] = strawberry.field(
        description="Nombre del rol a buscar.",
        default=None,
    )
    
    user_create: str = strawberry.field(
        description="Usuario que creo el rol."
    )
    
    user_update: str = strawberry.field(
        description="Ultimo usuario que modifico el rol."
    )

@strawberry.input(
    description="Input principal para obtener roles."
)
class GetUserRolesInput:
    filters: Optional[UserRoleFiltersInput] = strawberry.field(
        description="Filtros de búsqueda para roles.",
        default=None
    )

    pagination: Optional[PaginationInput] = strawberry.field(
        description="Configuración de paginación.",
        default=None
    )
# endregion


# ===================================
# region update rol input
# ===================================
@strawberry.input(
    description="Datos que puedes actualizar de un rol de usuario."
)
class UpdateUserRoleInput:
    id_user_role: UUID = strawberry.field(
        description="Id del rol a actualizar.",
    )
    
    name: Optional[str]  = strawberry.field(
        description="Nombre nuevo del rol."
    )
    
    description: Optional[str]  = strawberry.field(
        description="Descripción nueva del rol."
    )
# endregion


# ===================================
# region delete rol input
# ===================================
@strawberry.input(
    description="Eliminar el rol por id."
)
class DeleteUserRoleInput:
    id_user_role: UUID = strawberry.field(
        description="Id del rol a eliminar.",
    )
# endregion


# endregion
# ===============================================================================================================================================================================
# region USERS
# ===============================================================================================================================================================================



# ===================================
# region Enum statusUSer
# ===================================
@strawberry.enum(
    description="Estado del usuario"
)
class UserStatusEnum(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    BLOCKED = "BLOCKED"
    DELETED = "DELETED"


# ===================================
# region create user
# ===================================
@strawberry.input(
    description="Datos necesarios para crear un usuario."
)
class CreateUserInput:
    id_user_role: UUID = strawberry.field(
        description="ID del rol asignado al usuario."
    )

    name: str = strawberry.field(
        description="Nombre del usuario."
    )

    last_name: str = strawberry.field(
        description="Apellidos del usuario."
    )

    username: str = strawberry.field(
        description="Nombre de usuario único."
    )

    email: str = strawberry.field(
        description="Correo electrónico único del usuario."
    )

    password: str = strawberry.field(
        description="Contraseña del usuario (será almacenada hasheada)."
    )

    status: UserStatusEnum = strawberry.field(
        description="Estado inicial del usuario.",
        default=UserStatusEnum.ACTIVE
    )
    