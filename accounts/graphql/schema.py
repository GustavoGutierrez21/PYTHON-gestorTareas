import strawberry
from accounts.graphql.queries import UserRoleQuery
from accounts.graphql.mutations import UserRoleMutation, UsersMutation


@strawberry.type
class Mutation(UserRoleMutation, UsersMutation):
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
