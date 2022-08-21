import graphene
from graphene_django import DjangoObjectType
from . import models


class RoomType(DjangoObjectType):

    user = graphene.Field("users.types.UserType")
    is_fav = graphene.Boolean()

    class Meta:
        model = models.Room

    # ! 이 resolve는 custom resolve인데, 내가 방을 찾았을 때 그 방이 내가 fav에 등록한 방인지를 체크하려고 만든 resolve
    # ! 여기서 parent는 query를 수행했을 때 찾고자 했던 room이 될 것이고 info는 우리가 매번 쓰던 그 info
    def resolve_is_fav(parent, info):
        user = info.context.user
        if user.is_authenticated:
            return parent in user.favs.all()
        return False


class RoomsResponse(graphene.ObjectType):

    rooms = graphene.List(RoomType)
    total_count = graphene.Int()
