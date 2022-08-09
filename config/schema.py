import graphene
from rooms import schema as room_schema
from users import schema as user_schema


class Query(user_schema.Query, room_schema.Query, graphene.ObjectType):
    pass


class Mutation:
    pass


schema = graphene.Schema(query=Query)
