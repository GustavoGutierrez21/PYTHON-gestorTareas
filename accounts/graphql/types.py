import strawberry

from uuid import UUID
from datetime import datetime
from typing import Optional, List


# ===================================
# region Tabla Roles
# ===================================
@strawberry.type(
    description="Campos de un rol de usuario."
)
class UserRoleType:
    id_user_role: UUID = strawberry.field(
        description="Campos de la tabla user_role."
    )

    name: str = strawberry.field(
        description="Campos de la tabla user_role."
    )

    description: str | None = strawberry.field(
        description="Campos de la tabla user_role."
    )

    created_at: datetime = strawberry.field(
        description="Campos de la tabla user_role."
    )

    updated_at: datetime = strawberry.field(
        description="Campos de la tabla user_role."
    )
# endregion


# ===================================
# region create rol Response
# ===================================
@strawberry.type(
    description="Respuesta de salida al crear un rol de usuario."
)
class CreateUserRoleResponse:
    id: Optional[UUID] = strawberry.field(
        description="id unico de identificador."
    )

    status_code: int = strawberry.field(
        description="Status Code de respuesta."
    )

    message: str = strawberry.field(
        description="Mensaje de respuesta."
    )

    data: Optional[UserRoleType] = strawberry.field(
        description="Campos de la tabla user_role."
    )

    error: Optional[str] = strawberry.field(
        description="Razón del fallo."
    )
# endregion


# ===================================
# region see roles Response
# ===================================
@strawberry.type(
    description="Respuesta de salida al buscar roles de usuario."
)
class GetUserRoleResponse:
    id: Optional[UUID] = strawberry.field(
        description="id unico de identificador."
    )

    status_code: int = strawberry.field(
        description="Status Code de respuesta."
    )

    message: str = strawberry.field(
        description="Mensaje de respuesta."
    )
    
    total: Optional[int] = strawberry.field(
        description="Total de registros encontrados."
    )

    page: Optional[int] = strawberry.field(
        description="Número de página actual."
    )

    limit: Optional[int] = strawberry.field(
        description="Número de registros por página."
    )


    data: Optional[List['UserRoleType']] = strawberry.field(
        description="Lista de campos de la tabla user_role."
    )

    error: Optional[str] = strawberry.field(
        description="Razón del fallo."
    )
# endregion


# ===================================
# region update rol response
# ===================================
@strawberry.type(
    description="Respuesta de salida al actualizar un rol de usuario."
)
class UpdateUserRoleResponse:
    id: Optional[UUID] = strawberry.field(
        description="id unico de identificador."
    )

    status_code: int = strawberry.field(
        description="Status Code de respuesta."
    )

    message: str = strawberry.field(
        description="Mensaje de respuesta."
    )

    data: Optional[UserRoleType] = strawberry.field(
        description="Campos de la tabla user_role."
    )

    error: Optional[str] = strawberry.field(
        description="Razón del fallo."
    )
# endregion


# ===================================
# region delete rol response
# ===================================
@strawberry.type(
    description="Respuesta de salida al eliminar un rol de usuario."
)
class DeleteUserRoleResponse:
    id: Optional[UUID] = strawberry.field(
        description="id unico de identificador."
    )

    status_code: int = strawberry.field(
        description="Status Code de respuesta."
    )

    message: str = strawberry.field(
        description="Mensaje de respuesta."
    )

    error: Optional[str] = strawberry.field(
        description="Razón del fallo."
    )
# endregion