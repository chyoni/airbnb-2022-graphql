import graphene
import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from . import models
from rooms import models as room_models


class CreateAccountMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    ok = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, *args, **kwargs):
        email = kwargs["email"]
        password = kwargs["password"]
        first_name = kwargs["first_name"]
        last_name = kwargs["last_name"]
        try:
            models.User.objects.get(email=email)
            return CreateAccountMutation(ok=False, error="User already exists")
        except models.User.DoesNotExist:
            try:
                models.User.objects.create(
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                )
                return CreateAccountMutation(ok=True)
            except Exception:
                return CreateAccountMutation(ok=False, error="Can't create user")


class LoginMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    token = graphene.String()
    pk = graphene.Int()
    error = graphene.String()

    def mutate(self, info, *args, **kwargs):
        email = kwargs["email"]
        password = kwargs["password"]
        user = authenticate(username=email, password=password)
        if user:
            token = jwt.encode({"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256")
            return LoginMutation(token=token, pk=user.pk)
        else:
            return LoginMutation(error="Wrong username/password")


class ToggleFavsMutation(graphene.Mutation):
    class Arguments:
        room_id = graphene.Int(required=True)

    ok = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, *args, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("You need to be logged in")

        room_id = kwargs["room_id"]
        try:
            room = room_models.Room.objects.get(pk=room_id)
            if room in user.favs.all():
                user.favs.remove(room)
            else:
                user.favs.add(room)
            return ToggleFavsMutation(ok=True)
        except room_models.Room.DoesNotExist:
            return ToggleFavsMutation(ok=False, error="Room not found")
