import jwt
from django.conf import settings
from users import models as user_models


class JWTMiddleware(object):
    def resolve(self, next, root, info, **args):
        request = info.context

        token = request.META.get("HTTP_AUTHORIZATION")
        if token:
            try:
                decoded = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
                pk = decoded["pk"]
                user = user_models.User.objects.get(pk=pk)

                info.context.user = user
            except Exception:
                pass

        # ! middleware에서는 middleware를 거치면서 에러가 있던 없던 반드시 next를 호출해줘야 한다. 그래야 요청에 대한 resolver가 실행이 되기 때문에
        return next(root, info, **args)
