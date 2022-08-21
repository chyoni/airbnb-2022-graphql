# Airbnb API

REST & GraphQL API of the Airbnb Clone using Django REST Framework and Graphene GraphQL

### API Actions

- [ ] List Rooms
- [ ] Filter Rooms
- [ ] Search By Coords
- [ ] Login
- [ ] Create Account
- [ ] See Room
- [ ] Add Room to Favourites
- [ ] See Favs
- [ ] See Profile
- [ ] Edit Profile

### Index

- #01 Graphene - Django

  ```bash
  pipenv install graphene-django
  pipenv install graphql-core=2.3.1
  ```

  - 이렇게 해도 에러가 나는데 이유는 하나, Django에서 Graphql을 사용을 거의 안해서 업데이트가 안된듯하다.
    장고 >4.0 이상부터는 force_text 라는게 없는데 여전히 graphene_django는 사용중이다. 그래서 그걸 바꿔줘야 하는데
    방법은 아래와 같다.
    graphene_django > utils > utils.py 에서 6번라인

    remove this:

    ```bash
    from django.utils.encoding import force_text # Line 6
    s = force_text(s) # Line 29
    ```

    replace:

    ```bash
    from django.utils.encoding import force_str# Line 6
    s = force_str(s) # Line 29
    ```

- #02 Basic setting graphene

- #03 Room list by graphql

- #04 Room list pagniate and divide schema.py

- #05 See room and user

- #06 Mutation (create account)

  - mutations.py / queries.py 로 분리 후 schema.py에서 합치기 정리

- #07 JWT

  ```bash
  pipenv install pyjwt
  ```

- #08 Middlewares

  - Headers에 token을 넣고 request했을 때 token을 받아 decode하는 middleware

- #09 Me resolver
