import graphene
from . import types
from . import models


class Query(object):

    user = graphene.Field(types.UserType, id=graphene.Int(required=True))

    def resolve_user(self, info, id):
        return models.User.objects.get(pk=id)
