import strawberry


@strawberry.input(
    description="Datos necesarios para crear un rol de usuario."
)
class CreateUserRoleInput:
    """
    Input para crear un rol dentro del sistema.

    - name: Nombre único del rol (ej: ADMIN, EDITOR)
    - description: Descripción opcional del rol
    """
    name: str = strawberry.field(description="Nombre único del rol.")
    description: str = strawberry.field(description="Descripción del rol.")
