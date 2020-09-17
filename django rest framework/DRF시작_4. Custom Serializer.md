## Custom Serializer

- 우선 댓글 작성 로직을 먼저 작성한다.

```python
# community/urls.py

from django.urls import path
from . import views


app_name = 'community'

urlpatterns = [
    path('article/create/', views.article_create, name='article_create'),
    path('article/list/', views.article_list, name='article_list'),
    path('article/<int:article_id>/comment/create/', views.comment_create, name='comment_create'), # << 추가
]
```

```python
# community/views.py

from django.shortcuts import get_object_or_404

...

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)
    return Response(serializer.data)
```

- Response

```
{
    "content": "첫댓",
    "created_at": "2020-09-10T16:15:57.576086+09:00",
    "user": {
        "id": 2,
        "password": "pbkdf2_sha256$216000$TmqoDHCqAkx0$NIFiifJdo6OpVzsqGPSvOD537oh65+hAIEwRTM6oars=",
        "last_login": "2020-09-10T12:20:05.780087+09:00",
        "is_superuser": false,
        "username": "fortest",
        "first_name": "",
        "last_name": "",
        "email": "",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2020-09-10T12:20:05.637505+09:00",
        "groups": [],
        "user_permissions": []
    },
    "article": {
        "id": 1,
        "user": {
            "id": 2,
            "password": "pbkdf2_sha256$216000$TmqoDHCqAkx0$NIFiifJdo6OpVzsqGPSvOD537oh65+hAIEwRTM6oars=",
            "last_login": "2020-09-10T12:20:05.780087+09:00",
            "is_superuser": false,
            "username": "fortest",
            "first_name": "",
            "last_name": "",
            "email": "",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2020-09-10T12:20:05.637505+09:00",
            "groups": [],
            "user_permissions": []
        },
        "title": "제목을써보자",
        "content": "내용을써보겠",
        "created_at": "2020-09-10T12:56:15.681839+09:00",
        "updated_at": "2020-09-10T12:56:15.681839+09:00"
    }
}
```

- 근데 Response의 형식이 너무 복잡하다. 내가 쓰고싶은 항목만 골라서 Response로 줄 수 있을까?
- 그리고 날짜같은 경우 원하는 형식으로도 받을 수 있을까?

<br>

<br>

### 1. 원하는 필드만 Response로

#### a. 원하는 필드만 fields로 지정한 serializer를 만들어 사용한다.

먼저 `article_list`의 response를 살펴보자.

```
[
    {
        "id": 1,
        "user": {
            "id": 2,
            "password": "pbkdf2_sha256$216000$TmqoDHCqAkx0$NIFiifJdo6OpVzsqGPSvOD537oh65+hAIEwRTM6oars=",
            "last_login": "2020-09-10T12:20:05.780087+09:00",
            "is_superuser": false,
            "username": "fortest",
            "first_name": "",
            "last_name": "",
            "email": "",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2020-09-10T12:20:05.637505+09:00",
            "groups": [],
            "user_permissions": []
        },
        "title": "제목을써보자",
        "content": "내용을써보겠",
        "created_at": "2020-09-10T12:56:15.681839+09:00",
        "updated_at": "2020-09-10T12:56:15.681839+09:00"
    },
    {
        "id": 2,
        "user": {
            "id": 2,
            "password": "pbkdf2_sha256$216000$TmqoDHCqAkx0$NIFiifJdo6OpVzsqGPSvOD537oh65+hAIEwRTM6oars=",
            "last_login": "2020-09-10T12:20:05.780087+09:00",
            "is_superuser": false,
            "username": "fortest",
            "first_name": "",
            "last_name": "",
            "email": "",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2020-09-10T12:20:05.637505+09:00",
            "groups": [],
            "user_permissions": []
        },
        "title": "제목을써보자22",
        "content": "내용을써보겠22",
        "created_at": "2020-09-10T13:00:18.013220+09:00",
        "updated_at": "2020-09-10T13:00:18.014217+09:00"
    }
]
```

여기서 유저의 이름, 이메일, 마지막 로그인 시간만 보고싶다.

그러면 User를 직렬화하는 또다른 `serializer`를 만들 수 있다.

```python
# accounts/serializers.py

from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ArticleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_login']
```

- Article 모델에 사용할 `ArticleUserSerializer`를 만들어서 사용한다.

```python
# community/serializers.py

...
from accounts.serializers import UserSerializer, ArticleUserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    user = ArticleUserSerializer(required=False)
    class Meta:
        model = Article
        fields = '__all__'

...
```

- Response는 다음과 같이 나온다.

```
[
    {
        "id": 1,
        "user": {
            "username": "fortest",
            "email": "",
            "last_login": "2020-09-10T12:20:05.780087+09:00"
        },
        "title": "제목을써보자",
        "content": "내용을써보겠",
        "created_at": "2020-09-10T12:56:15.681839+09:00",
        "updated_at": "2020-09-10T12:56:15.681839+09:00"
    },
    {
        "id": 2,
        "user": {
            "username": "fortest",
            "email": "",
            "last_login": "2020-09-10T12:20:05.780087+09:00"
        },
        "title": "제목을써보자22",
        "content": "내용을써보겠22",
        "created_at": "2020-09-10T13:00:18.013220+09:00",
        "updated_at": "2020-09-10T13:00:18.014217+09:00"
    }
]
```

<br>

#### b. 한 개만 추가하고 싶은 경우

- 미리 django rest framework에서 정의된 field를 이용하면 된다.
  - StringRelatedField - `__str__` 메소드를 이용한 내용을 표시할 때 쓸 수 있다.
  - PrimaryKeyRelatedField - 고유키를 표시한다.
  - HyperlinkedRelatedField - hyperlink를 표시한다.
  - SlugRelatedField - field 하나를 사용해서 표시한다.

위의 `article_list`에 대한 Response에 댓글의 내용만 모아서 같이 보고싶다고 해보자. 그러면 `SlugRelatedField`를 이용하여 `content` 필드를 지정해서 함께 보여줄 수 있을 것이다.

```python
# community/serializers.py

...
from accounts.serializers import UserSerializer, ArticleUserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    user = ArticleUserSerializer(required=False)
    comments = serializers.SlugRelatedField(many=True, read_only=True, slug_field='content')
    class Meta:
        model = Article
        fields = '__all__'

...
```

- Response는 다음과 같이 나온다.

```
[
    {
        "id": 1,
        "user": {
            "username": "fortest",
            "email": "",
            "last_login": "2020-09-10T12:20:05.780087+09:00"
        },
        "comments": [
            "첫댓"
        ],
        "title": "제목을써보자",
        "content": "내용을써보겠",
        "created_at": "2020-09-10T12:56:15.681839+09:00",
        "updated_at": "2020-09-10T12:56:15.681839+09:00"
    },
    {
        "id": 2,
        "user": {
            "username": "fortest",
            "email": "",
            "last_login": "2020-09-10T12:20:05.780087+09:00"
        },
        "comments": [],
        "title": "제목을써보자22",
        "content": "내용을써보겠22",
        "created_at": "2020-09-10T13:00:18.013220+09:00",
        "updated_at": "2020-09-10T13:00:18.014217+09:00"
    }
]
```

- `id=1`인 글에만 `"첫댓"`이라는 내용의 댓글이 하나 달려있으므로 위와 같이 Response 형식이 갖춰짐을 알 수 있다.

<br>

<br>

### 2. 형식 커스터마이징

#### a. RelatedField와 to_representation 메소드 사용

- 외래 키를 사용한 게 아니라 자신 고유의 속성이 표시되는 형식을 바꾸고 싶다면 `RelatedField` 대신 `Field`를 상속받아서 할 수 있다.
- `"comments"`에 댓글 내용만 덩그러니 오는 것을 바꿔보자. 어떤 유저가 해당 내용을 썼는지의 형식으로 바꿔보겠다.

```python
# community/serializers.py

...

class CommentListingField(serializers.RelatedField):
    def to_representation(self, value):
        return f'{value.user.username}님이 쓴 내용: {value.content}'

class ArticleSerializer(serializers.ModelSerializer):
    user = ArticleUserSerializer(required=False)
    # comments = serializers.SlugRelatedField(many=True, read_only=True, slug_field='content')
    comments = CommentListingField(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        
...
```

- `serializers.RelatedField`를 상속받은 후, `to_representation`메소드를 사용하여 어떤 형식으로 보여줄지 정할 수 있다.
- `value`에는 모델 객체가 들어오고, 이 경우엔 댓글 객체가 각각 들어가므로 `to_representation` 함수 내에서 `value`는 comment이다.
- Response는 다음과 같이 나온다.

```
[
    {
        "id": 1,
        "user": {
            "username": "fortest",
            "email": "",
            "last_login": "2020-09-10T12:20:05.780087+09:00"
        },
        "comments": [
            "fortest님이 쓴 내용: 첫댓"
        ],
        "title": "제목을써보자",
        "content": "내용을써보겠",
        "created_at": "2020-09-10T12:56:15.681839+09:00",
        "updated_at": "2020-09-10T12:56:15.681839+09:00"
    },
    {
        "id": 2,
        "user": {
            "username": "fortest",
            "email": "",
            "last_login": "2020-09-10T12:20:05.780087+09:00"
        },
        "comments": [],
        "title": "제목을써보자22",
        "content": "내용을써보겠22",
        "created_at": "2020-09-10T13:00:18.013220+09:00",
        "updated_at": "2020-09-10T13:00:18.014217+09:00"
    }
]
```

<br>

#### b. SerializerMethodField

- `SerializerMethodField(method_name=None)`
- `read-only` field이다.
- 예를 들어, `days = serializers.SerializerMethodField`와 같이 한다면 `get_days`라는 함수를 만들어서 표시 형식을 정할 수 있다.
- `comments` 부분에 지금은 내용만 가져오지만, 필요한 정보들을 원하는 순서대로 가져오는 등 원하는 대로 커스터마이징 할 수 있다.

```python
# community/serializers.py

...

class CommentListingField(serializers.RelatedField):
    def to_representation(self, value):
        return f'{value.user.username}님이 쓴 내용: {value.content}'

class ArticleSerializer(serializers.ModelSerializer):
    user = ArticleUserSerializer(required=False)
    # comments = serializers.SlugRelatedField(many=True, read_only=True, slug_field='content')
    # comments = CommentListingField(many=True, read_only=True)   
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    def get_comments(self, article):
        comments = Comment.objects.filter(article=article).order_by('-created_at')
        serializer = CommentForArticleSerializer(instance=comments, many=True)
        return serializer.data

class CommentForArticleSerializer(serializers.ModelSerializer):
    user = ArticleUserSerializer
    class Meta:
        model = Comment
        fields = ['content', 'created_at', 'user']
        
...
```

- 기존에 정의했던 `CommentSerializer`를 사용하게 되면 ` article`을 필드로 포함하고 있기때문에 무한루프를 돌며 에러가 난다. 그래서 `article`필드를 포함하지 않는 `CommentForArticleSerializer`라는 클래스를 새로 정의하여 사용했다.
- Response는 다음과 같이 나온다.

```
[
    {
        "id": 1,
        "user": {
            "username": "fortest",
            "email": "",
            "last_login": "2020-09-10T12:20:05.780087+09:00"
        },
        "comments": [
            {
                "content": "첫댓",
                "created_at": "2020-09-10T16:15:57.576086+09:00",
                "user": 2
            }
        ],
        "title": "제목을써보자",
        "content": "내용을써보겠",
        "created_at": "2020-09-10T12:56:15.681839+09:00",
        "updated_at": "2020-09-10T12:56:15.681839+09:00"
    },
    {
        "id": 2,
        "user": {
            "username": "fortest",
            "email": "",
            "last_login": "2020-09-10T12:20:05.780087+09:00"
        },
        "comments": [],
        "title": "제목을써보자22",
        "content": "내용을써보겠22",
        "created_at": "2020-09-10T13:00:18.013220+09:00",
        "updated_at": "2020-09-10T13:00:18.014217+09:00"
    }
]
```

- 댓글을 2개 더 작성한 후의 Response는 다음과 같이 최신순으로 정렬되어 반환되는 것을 볼 수 있다.

```
[
    {
        "id": 1,
        "user": {
            "username": "fortest",
            "email": "",
            "last_login": "2020-09-10T12:20:05.780087+09:00"
        },
        "comments": [
            {
                "content": "돈두댓",
                "created_at": "2020-09-11T15:06:52.878628+09:00",
                "user": 2
            },
            {
                "content": "댓",
                "created_at": "2020-09-11T15:06:38.453445+09:00",
                "user": 2
            },
            {
                "content": "첫댓",
                "created_at": "2020-09-10T16:15:57.576086+09:00",
                "user": 2
            }
        ],
        "title": "제목을써보자",
        "content": "내용을써보겠",
        "created_at": "2020-09-10T12:56:15.681839+09:00",
        "updated_at": "2020-09-10T12:56:15.681839+09:00"
    },
    {
        "id": 2,
        "user": {
            "username": "fortest",
            "email": "",
            "last_login": "2020-09-10T12:20:05.780087+09:00"
        },
        "comments": [],
        "title": "제목을써보자22",
        "content": "내용을써보겠22",
        "created_at": "2020-09-10T13:00:18.013220+09:00",
        "updated_at": "2020-09-10T13:00:18.014217+09:00"
    }
]
```

<br>

<br>

<br>

<br>

참고자료

- [Django REST framework Documentations](https://www.django-rest-framework.org/)