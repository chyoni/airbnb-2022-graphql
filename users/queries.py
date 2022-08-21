from . import models


def resolve_user(root, info, id):
    print(info, id)
    return models.User.objects.get(id=id)


def resolve_me(root, info):
    user = info.context.user
    if user.is_authenticated:
        return info.context.user
    else:
        raise Exception("You need to be logged in")
