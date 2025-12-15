import strawberry
from accounts.graphql.schema import Mutation as AccountsMutation
from accounts.graphql.schema import UserRoleQuery


@strawberry.type
class Query(UserRoleQuery):
    @strawberry.field
    def hello(self) -> str:
        return "Hola mundo!"


@strawberry.type
class Mutation(AccountsMutation):
    """
    Mutations globales
    (hereda las de accounts)
    """
    pass


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
