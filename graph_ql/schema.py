import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hola mundo!"


schema = strawberry.Schema(query=Query)
