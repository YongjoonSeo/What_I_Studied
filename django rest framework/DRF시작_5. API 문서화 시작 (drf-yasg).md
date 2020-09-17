## API 문서화 (drf-yasg)

- 원래 `django-rest-swagger`가 많이 쓰이고 있었지만 생을 마감했다고 한다..
  - [생을 마감한 패키지 - django-rest-swagger](https://github.com/marcgibbons/django-rest-swagger)
  - 이 깃허브에서도 볼 수 있듯 `drf-yasg`를 API 문서화 도구로 고려하라고 한다.

<br>

<br>

## drf-yasg

### 1. 설치

- `pip install drf-yasg` 명령어를 통해 설치한다.

- `settings.py`의 `INSTALLED_APPS` 변수에 `'drf_yasg'`를 등록한다.

  ```python
  # settings.py
  
  ...
  
  INSTALLED_APPS = [
      # default
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'django.contrib.sites', # registration
  
      # DRF
      'rest_framework',
      'rest_framework.authtoken',
  
      # rest-auth & allauth
      'rest_auth',
      'allauth',
      'allauth.account',
      'rest_auth.registration',
  
      # CORS
      'corsheaders',
  
      # swagger
      'drf_yasg',
  
      # my apps
      'accounts',
      'community',
  ]
  
  ...
  ```

<br>

<br>

### 2. Swagger 문서 endpoint지정

- 프로젝트 폴더의 `urls.py`를 다음과 같이 구성한다.

  ```python
  # urls.py
  
  from django.contrib import admin
  from django.urls import path, include
  from rest_framework import permissions								# <<< 추가됨
  from drf_yasg.views import get_schema_view							# <<< 추가됨
  from drf_yasg import openapi										# <<< 추가됨
  
  schema_view = get_schema_view(										# <<< 추가됨
     openapi.Info(													# <<< 추가됨
        title="나의 API",											   # <<< 추가됨
        default_version='v1',											# <<< 추가됨
        description="문서화 하는 중입니다.",							  # <<< 추가됨
        terms_of_service="https://www.google.com/policies/terms/",	# <<< 추가됨
        contact=openapi.Contact(email="myemail@gmail.com"),			# <<< 추가됨
        license=openapi.License(name="myApp's License"),				# <<< 추가됨
     ),																# <<< 추가됨
     public=True,														# <<< 추가됨
     permission_classes=(permissions.AllowAny,),						# <<< 추가됨
  )																	# <<< 추가됨
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('rest-auth/', include('rest_auth.urls')), # rest_auth url 등록
      path('rest-auth/registration/', include('rest_auth.registration.urls')), # 회원가입
      path('community/', include('community.urls')), # community app
      path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # swagger	# <<< 추가됨
  ]
  ```

  - `openapi.info`의 인자로 들어가는 `title`은 API 문서의 제목을 지칭한다.
  - `default_version`은 표시할 버전을 나타낸다.
  - `description`은 API 문서의 설명을 나타낸다.
  - `contact`는 개발자의 email을 나타낸다.
  - `licence`로 API 문서 소개 바로 밑에 원하는 licence를 표시할 수 있다.
  - 여러 가지의 endpoint를 설정할 수 있다. 
    - 여기선 `swagger UI`로 보도록 설정했지만 (`schema_view.with_ui('swagger'`부분) `redoc`과 같은 UI로도 볼 수 있다. [공식문서 참고](https://drf-yasg.readthedocs.io/en/stable/readme.html#quickstart)

- `python manage.py runserver` 명령어를 통해 서버를 실행하여 `http://localhost:8000/swagger/`로 접속하면 다음 화면을 볼 수 있다.

<details><summary>swagger 설정 후 첫 화면</summary><img src="https://i.ibb.co/528S3Tr/swagger1.jpg"><img src="https://i.ibb.co/2ZYbbG0/swagger2.jpg"><img src="https://i.ibb.co/Tg5grb9/swagger3.jpg"></details>

<br>

<br>

### 3. Docstring 사용

- Docstring은 큰 따옴표 세 개 `"""` 를 이용하여 적은 내용이며 문서에서 보여지는 부분이다.
  - 작은 따옴표를 써도 여러 줄의 문자열을 만들 수 있지만, 항상 큰 따옴표를 쓰도록 한다. [Convention 참고](https://www.python.org/dev/peps/pep-0257/#what-is-a-docstring)

초기 세팅 대로 문서를 확인하면 다음과 같이 나타난다.

![initial](https://i.ibb.co/5nW7c54/swagger-docstring1.jpg)

아무런 설명도 없으므로 어떤 내용인지 쉽게 파악하기 힘들다.

해당 요청주소는 `community` 앱 안의 `article_create`함수를 호출하기 위한 것이므로 `community/views.py`에서 API문서의 설명을 붙일 수 있다.

```python
# community/views.py

...

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_create(request):
    """
    게시글 생성

    ## 게시글 생성
    - 로그인한 사용자만 요청할 수 있다.
    """
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
    return Response(serializer.data)

...
```

- 커밋 메시지를 쓸 때 처럼 마크다운 문법을 쓸 수 있다.
  - 커밋 제목과 내용 사이에 한 줄의 간격이 있는 것처럼 이 docstring에서도 마찬가지 방법을 적용해야 제목과 내용을 구분할 수 있다.
- 결과는 다음과 같이 된다.

![after_docstring](https://i.ibb.co/8B53wfM/swagger-docstring2.jpg)

<br>

<br>

<br>

<br>

- 참고자료
  - [drf-yasg Documentation](https://drf-yasg.readthedocs.io/en/stable/index.html)
  - [운동하는 개발자 Fitware Jay님의 블로그](https://jay-ji.tistory.com/31)
  - [rubycho님의 블로그](https://velog.io/@rubycho/%EB%AC%B8%EC%84%9C%ED%99%94%EB%A5%BC-%EC%9C%84%ED%95%9C-drf-yasg-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0#custom-response)
  - [타운컴퍼니 기술블로그](https://medium.com/towncompany-engineering/%EC%B9%9C%EC%A0%88%ED%95%98%EA%B2%8C-django-rest-framework-api-%EB%AC%B8%EC%84%9C-%EC%9E%90%EB%8F%99%ED%99%94%ED%95%98%EA%B8%B0-drf-yasg-c835269714fc)