import strawberry

from uuid import UUID
from datetime import datetime
from typing import Optional


@strawberry.type(
    description="Campos de un rol de usuario."
)
class UserRoleType:
    id_user_role: UUID = strawberry.field(
        description="Campos de la tabla user_role.")

    name: str = strawberry.field(
        description="Campos de la tabla user_role.")

    description: str | None = strawberry.field(
        description="Campos de la tabla user_role.")

    created_at: datetime = strawberry.field(
        description="Campos de la tabla user_role.")

    updated_at: datetime = strawberry.field(
        description="Campos de la tabla user_role.")


@strawberry.type(
    description="Respuesta de salida al crear un rol de usuario."
)
class UserRoleResponse:
    id: Optional[UUID] = strawberry.field(
        description="id unico de identificador.")

    status_code: int = strawberry.field(
        description="Status Code de respuesta.")

    message: str = strawberry.field(description="Mensaje de respuesta.")

    data: Optional[UserRoleType] = strawberry.field(
        description="Campos de la tabla user_role.")

    error: Optional[str] = strawberry.field(description="Razón del fallo.")
