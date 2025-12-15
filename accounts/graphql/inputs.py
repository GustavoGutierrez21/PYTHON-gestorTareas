import strawberry
from uuid import UUID
from typing import Optional


@strawberry.input(
    description="Datos necesarios para crear un rol de usuario."
)
class CreateUserRoleInput:
    name: str = strawberry.field(description="Nombre único del rol.")
    description: str = strawberry.field(description="Descripción del rol.")


@strawberry.input(
    description="Datos necesarios para crear un rol de usuario."
)
class GetUserRoleInput:
    id: Optional[UUID] = strawberry.field(
        description="Id del rol a buscar.",
        default=None,
    )

    name: Optional[str] = strawberry.field(
        description="Nombre del rol a buscar.",
        default=None,
    )
