## django REST API 개발을 위한 설정

### 1. 기타 패키지 설치

#### a. django-rest-auth

- 로그인, 로그아웃 등 회원관리를 하기 위한 패키지이다.

- 소셜로그인을 구현하는 데도 필요하다.

- django의 token을 기반으로 인증관리를 한다.

- 회원가입도 구현하고자 하면 `django-allauth` 패키지가 필요하다.

- `pip install django-rest-auth` 명령어를 통해 설치한다.

- `settings.py`의 `INSTALLED_APPS` 변수에 `'rest_framework'`,  `'rest_framework.authtoken'`, `'rest_auth'`를 추가한다. 또한, `django-rest-auth`는 django의 token을 기반으로 인증관리를 하므로 **token에 대한 설정**을 해줘야 한다.

  ```python
  # settings.py
  
  INSTALLED_APPS = [
      # default
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  
      # DRF
      'rest_framework',
      'rest_framework.authtoken',
  
      # rest-auth
      'rest_auth',
  ]
  
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [
          'rest_framework.authentication.TokenAuthentication',
      ]
  }
  ```

  - `'rest_framework'`는 `djangorestframework`를 설치할 때 등록했으므로 나머지 두 개만 작성하였다.

- 프로젝트 폴더 내의 최상위 `urls.py`에 다음과 같이 url 패턴을 등록한다.

  ```python
  # urls.py
  
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('rest-auth/', include('rest_auth.urls')), # rest_auth url 등록
  ]
  ```

<br>

#### b. django-allauth

- 소셜로그인을 위해 필요한 패키지이다.

  - `django-rest-auth` 패키지도 필요하다.

- `pip install django-allauth` 명령어를 통해 설치한다.

- `settings.py`의 `INSTALLED_APPS` 변수에 `'allauth'`, `'allauth.account'`, `'rest_auth.registration'`, `'django.contrib.sites'`를 추가하고, `SITE_ID = 1`로 변수를 하나 추가한다.

  ```python
  # settings.py
  
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
  ]
  
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [
          'rest_framework.authentication.TokenAuthentication',
      ]
  }
  
  # django-allauth
  SITE_ID = 1
  ```

  - `django-allauth`와 `django-rest-auth`를 모두 설치하고, `'rest_auth.registration'`을 `settings.py`에 등록하여 회원가입을 구현할 수 있다.

- 프로젝트 폴더 내의 최상위 `urls.py`에 다음과 같이 url 패턴을 등록한다.

  ```python
  # urls.py
  
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('rest-auth/', include('rest_auth.urls')), # rest_auth url 등록
      path('rest-auth/registration/', include('rest_auth.registration.urls')), # 회원가입
  ]
  ```

<br>

#### c. django-cors-headers

- 브라우저의 CORS (Cross-Origin Resource Sharing) 정책에 의해 요청이 막히는 문제를 해결하기 위한 패키지이다.

- `pip install django-cors-headers` 명령어를 통해 설치한다.
- `settings.py`의 `INSTALLED_APPS` 변수에 `'corsheaders'`를 추가하고, `MIDDLEWARE` 변수에 `'corsheaders.middleware.CorsMiddleware'`를 추가한다.
  
- `MIDDLEWARE` 변수에 추가할 때 적어도 `'django.middle.common.CommonMiddleware'` 위에 위치해야 한다.
  
- 개발 단계에서는 `settings.py`에 `CORS_ORIGIN_ALLOW_ALL = True`라고 설정하고, 추후 배포할 땐 `CORS_ORIGIN_WHITELIST`를 사용하여 특정 사이트로부터의 요청만 허용하게 할 수 있다.

  ```python
  # settings.py
  
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
  ]
  
  MIDDLEWARE = [
      'corsheaders.middleware.CorsMiddleware', # CORS
      'django.middleware.security.SecurityMiddleware',
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.middleware.common.CommonMiddleware',
      'django.middleware.csrf.CsrfViewMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
      'django.middleware.clickjacking.XFrameOptionsMiddleware',
  ]
  
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [
          'rest_framework.authentication.TokenAuthentication',
      ]
  }
  
  # django-allauth
  SITE_ID = 1
  
  # CORS
  # 배포시 CORS_ORIGIN_WHITELIST 사용하기.
  CORS_ORIGIN_ALLOW_ALL = True
  ```

<br>

#### 참고: requirements.txt

- `pip freeze > requirements.txt` 명령어를 통해 현재까지 설치한 pip 패키지의 목록을 저장할 수 있다.
- `requirements.txt`가 있는 디렉토리에서 `pip install -r requirements.txt` 명령어를 통해 현재 프로젝트에 필요한 모든 패키지를 설치할 수 있다.

<br>

<br>

### 2. app 생성

- 프로젝트를 시작하기 전 커스텀 유저 모델을 만들어두는 게 좋다.

  - 나중에 유저에 어떤 요소를 추가하더라도 모델을 미리 만들어두어야 변경하기 쉽다.

- `manage.py`가 있는 디렉토리에서 `python manage.py startapp {app 이름}` 명령어를 통해 app을 만들 수 있다.

  - `python manage.py startapp accounts` 명령어를 통해 accounts라는 app을 만들 수 있다.
  - app을 만들고 나면 항상 `settings.py`의 `INSTALLED_APPS`에 추가해줘야 한다.

  ```python
  # settings.py
  
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
  
      # my apps
      'accounts',
  ]
  ```

- `accounts/models.py`에 `AbstractUser`를 이용하여 커스텀 유저 모델을 만들어둔다.

  ```python
  # accounts/models.py
  
  from django.db import models
  from django.contrib.auth.models import AbstractUser
  
  # Create your models here.
  class User(AbstractUser):
      pass
  ```

- `settings.py`에서 `AUTH_USER_MODEL = 'accounts.User'` 변수를 등록하여 방금 만든 커스텀 유저 모델을 기본 유저 모델로 등록한다.

  ```python
  # settings.py
  
  ...
  AUTH_USER_MODEL = 'accounts.User'
  ...
  ```

- 설정이 끝난 후엔  `manage.py`가 있는 디렉토리에서 데이터베이스에 연동해주는 명령어를 입력한다. 

  - 스키마를 생성하기 위해 `python manage.py makemigrations`를 입력한다.
  - 데이터베이스에 반영하기 위해 `python manage.py migrate`를 입력한다.

<br>

<br>

### 3. 관리자 계정 생성

- `manage.py`가 있는 디렉토리에서 `python manage.py createsuperuser` 명령어를 통해 관리자 계정을 만들 수 있다.
- 추후에 만든 app 내부의 `admin.py`를 수정하여 관리자 페이지를 수정할 수 있다.