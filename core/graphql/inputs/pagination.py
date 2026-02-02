import strawberry

@strawberry.input(
    description="Parámetros de paginación."
)
class PaginationInput:
    page: int = strawberry.field(
        description="Número de página.",
        default=1
    )

    limit: int = strawberry.field(
        description="Registros por página.",
        default=10
    )