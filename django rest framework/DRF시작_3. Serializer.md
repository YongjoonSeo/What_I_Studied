## Serializer

- Serializer는 쿼리셋이나 모델 객체를 JSON 혹은 XML 형태로 쉽게 변환할 수 있게 해준다.

<br>

### 1. 기본 세팅

- 현재 디렉토리 구조 & 모델들의 형태

  ![현재디렉토리](https://i.ibb.co/jvGrsz9/directory-serializer.jpg)
  - community라는 app을 만들었다. (`python manage.py startapp community`)

  - 위 사진의 `Article`, `Comment` 모델을 사용하여 Serializer를 만들 것이다.

  - app을 만들면 보통 하는 작업을 해놓은 상태이다.

    - `settings.py`의 `INSTALLED_APPS`에 `'community'`를 추가한다.

    - community app 내부에 urls.py를 만들고 urlpatterns를 정의한다.

      ```python
      # community/urls.py
      
      from django.urls import path
      
      
      app_name = 'community'
      
      urlpatterns = []
      ```

    - 프로젝트 폴더 내부 urls.py에 community url을 include를 사용하여 포함한다.

      ```python
      # pracpjt2/urls.py
      
      from django.contrib import admin
      from django.urls import path, include
      
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('rest-auth/', include('rest_auth.urls')), # rest_auth url 등록
          path('rest-auth/registration/', include('rest_auth.registration.urls')), # 회원가입
          path('community/', include('community.urls')), # community app <<< 추가된 부분
      ]
      ```

- 만들어둔 앱 내부에 `serializers.py`라는 파일을 만들어서 관리하면 좋다.

<br>

<br>

### 2. ModelSerializer

- Django 모델을 JSON형태로 건네주기 위한 전처리 기능을 한다. = 직렬화한다.

```python
# accounts/serializers.py

from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
```

- `class Meta`부분에 해당 serializer의 정보를 적는다.
  - `model`: 어떤 모델을 직렬화할지 정한다.
  - `fields`: 해당 모델의 어떤 필드(칼럼)을 사용할지 표기한다. `'__all__'`과 같이 나타내면 모든 필드를 사용한다는 뜻이다.

```python
# community/serializers.py

from rest_framework import serializers
from .models import Article, Comment
from accounts.serializers import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    article = ArticleSerializer(required=False)
    class Meta:
        model = Comment
        fields = ['content', 'created_at', 'user', 'article']
```

- `ForeignKey`로 연결된 필드는 해당 serializer를 들고온다. (user)
- `UserSerializer`에 `required=False`옵션은 추후에 `views.py`에서 article을 만들거나 수정하는 과정에서 유효성 검사할 때 곧바로 예외처리 되지 않도록 하기 위함이다.
- `CommentSerializer`의 `fields = ['content', 'created_at', 'user', 'article']`처럼 사용하고 싶은 일부 필드를 적는 것도 가능하다.

<br>

<br>

### 3. 직렬화 데이터 전송

- 직렬화된 데이터를 응답으로 전송하기 위해 요청 보낼 주소를 `urls.py`에 적고, `views.py`에 로직을 작성한다.

```python
# community/urls.py

from django.urls import path
from . import views


app_name = 'community'

urlpatterns = [
    path('article/create/', views.article_create, name='article_create'),
    path('article/list/', views.article_list, name='article_list'),
]
```

```python
# community/views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
```

- `@permission_classes([IsAuthenticated])`를 통해 게시글을 생성하거나 목록을 조회할 때 모두 로그인 되어야만 하도록 설정했다.
- `@api_view`를 통해 원하는 HTTP 요청에 따라 해당 함수가 실행되도록 하고, `Response`를 통해 데이터를 전송한다.
- `Article`모델의 칼럼 중 `ForeignKey`로 정의되어있는 `user`칼럼은 유효성 검사 이후 serializer를 저장할 때 키워드 인자로 넣어줘야 한다.
- `article_list`에서 많은 수의 article이 들어갈 때는 serializer에 `many=True`옵션을 준다.
- 댓글에 대한 로직은 위와 동일하다.

<br>

- 먼저 글을 써보기 전에 `django-rest-auth`의 [API endpoint](https://django-rest-auth.readthedocs.io/en/latest/api_endpoints.html)를 참고하여 계정을 하나 만든다.

<details><summary>Postman을 이용하여 회원가입 한 결과</summary><img src="https://i.ibb.co/2qCChxj/registration.jpg"></details>

<br>

- 헤더에 `Authorization`이라는 키 값으로 `Token {토큰키 값}`을 넣어서 전송해야 인증된 사용자의 권한을 가진다.
- Response

```
# Response - article_create

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
}
```

```
# Response - article_list

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

<br>

<br>

<br>

<br>

참고자료

- [Django REST framework Documentations](https://www.django-rest-framework.org/)