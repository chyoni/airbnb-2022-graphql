import graphene
from . import types
from . import models


class Query(object):
    rooms = graphene.Field(types.RoomsResponse, page=graphene.Int())
    room = graphene.Field(types.RoomType, id=graphene.Int(required=True))

    def resolve_rooms(self, info, page=1):
        if page < 1:
            page = 1
        page_size = 5
        offset = page_size * (page - 1)
        limit = page_size * page
        rooms = models.Room.objects.all()[offset:limit]
        total_count = models.Room.objects.count()
        return types.RoomsResponse(rooms=rooms, total_count=total_count)

    def resolve_room(self, info, id):
        return models.Room.objects.get(pk=id)
