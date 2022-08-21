import graphene
import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from . import models


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
