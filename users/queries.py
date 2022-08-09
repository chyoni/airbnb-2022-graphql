from . import models


def resolve_user(self, info, id):
    print(info, id)
    return models.User.objects.get(id=id)
