import strawberry
from accounts.graphql.mutations import UserRoleMutation
from accounts.graphql.queries import UserRoleQuery


@strawberry.type
class Mutation(UserRoleMutation):
    """
    Schema de mutations del módulo accounts
    """
    pass


@strawberry.type
class Query(UserRoleQuery):
    """
    Schema de mutations del módulo accounts
    """
    pass
