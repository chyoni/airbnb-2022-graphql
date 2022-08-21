import graphene
from . import types
from . import models
from . import mutations
from . import queries


class Query(object):

    user = graphene.Field(
        types.UserType, id=graphene.Int(required=True), resolver=queries.resolve_user
    )
    me = graphene.Field(types.UserType, resolver=queries.resolve_me)


class Mutation(object):

    create_account = mutations.CreateAccountMutation.Field()
    login = mutations.LoginMutation.Field()
    toggle_favs = mutations.ToggleFavsMutation.Field()
    edit_profile = mutations.EditProfileMutation.Field()
