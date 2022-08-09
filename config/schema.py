import graphene
from graphene_django import DjangoObjectType
from rooms import models as room_models


class RoomObjectType(DjangoObjectType):
    class Meta:
        model = room_models.Room


class Query(graphene.ObjectType):
    hello = graphene.String()
    rooms = graphene.List(RoomObjectType)

    def resolve_hello(self, info):
        return "Hello"

    def resolve_rooms(self, info):
        return room_models.Room.objects.all()


class Mutation:
    pass


schema = graphene.Schema(query=Query)
