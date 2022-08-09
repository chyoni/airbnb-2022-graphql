import graphene
from . import types
from . import queries


class Query(object):
    rooms = graphene.Field(
        types.RoomsResponse, page=graphene.Int(), resolver=queries.resolve_rooms
    )
    room = graphene.Field(
        types.RoomType, id=graphene.Int(required=True), resolver=queries.resolve_room
    )
