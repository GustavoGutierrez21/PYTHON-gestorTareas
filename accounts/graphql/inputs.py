import strawberry
from uuid import UUID
from typing import Optional

from core.graphql.inputs.pagination import PaginationInput


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