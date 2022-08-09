import graphene
from graphene_django import DjangoObjectType
from . import models


class RoomObjectType(DjangoObjectType):
    class Meta:
        model = models.Room


class Query(object):
    rooms = graphene.List(RoomObjectType, page=graphene.Int())

    def resolve_rooms(self, info, page=1):
        page_size = 5
        offset = page_size * (page - 1)
        limit = page_size * page
        return models.Room.objects.all()[offset:limit]
