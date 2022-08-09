import graphene
from graphene_django import DjangoObjectType
from . import models


class RoomType(DjangoObjectType):

    user = graphene.Field("users.types.UserType")

    class Meta:
        model = models.Room


class RoomsResponse(graphene.ObjectType):

    rooms = graphene.List(RoomType)
    total_count = graphene.Int()
