import strawberry
from accounts.graphql.mutations import UserRoleMutation


@strawberry.type
class Mutation(UserRoleMutation):
    """
    Schema de mutations del módulo accounts
    """
    pass
