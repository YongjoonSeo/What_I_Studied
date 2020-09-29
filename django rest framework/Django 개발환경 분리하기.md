## Django 개발환경 분리하기

### 1. 개발환경 분리 이유

- 개발 환경이랑 배포 환경에서 `settings.py`의 설정이 달라야 하는 경우가 있다.
  - 특히 `DEBUG = TRUE`부분은 배포할 때 반드시 바꿔야하기 때문에 개발할 때와 필연적으로 설정이 달라지게 된다.
- 이외에도 데이터베이스를 나눠서 사용할 수도 있으며, 원하는 대로 설정을 분리하여 사용하면 개발 환경과 배포 환경을 독립적으로 관리하는 데 효과적이다.

<br>

<br>

### 2. settings.py 분리

#### a. 파일 분리

- 프로젝트 폴더 안에 `settings`와 같은 이름을 가진 폴더를 하나 만들자.

- `settings.py`를 로컬 환경에서 사용할 `local.py`, 협업 개발 환경에서 사용할 `development.py`, 배포 환경에서 사용할 `production.py`, 공통으로 사용할 `base.py`로 나누고 `settings`폴더가 django의 세팅이 되도록 `__init__.py`도 만들어준다.

- 프로젝트 폴더 디렉토리 구조

  ```
  pracpjt2
  │  urls.py
  │  wsgi.py
  │  __init__.py
  │
  ├─settings
  │  │  base.py
  │  │  development.py
  │  │  local.py
  │  │  production.py
  │  │  __init__.py
  │  └─__pycache__
  └─__pycache__
  ```

  - 기존에 `pracpjt2` (프로젝트 폴더) 내부에 있던 `settings.py`를 없애고 `settings`폴더를 만들어 분리했다.

- **base.py**

  ```python
  # settings/base.py
  
  import os, json
  from django.core.exceptions import ImproperlyConfigured
  
  
  class Secrets:
      def __init__(self, secret_file):
          with open(secret_file) as f:
              self.secrets = json.loads(f.read())
      
      def get_secret(self, setting):
          try:
              return self.secrets.get(setting)
          except:
              error_msg = f'Set the {setting} environment variable'
              raise ImproperlyConfigured(error_msg)
  
  # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
  
  secret_file = os.path.join(BASE_DIR, 'secrets.json')
  secrets = Secrets(secret_file)
  
  SECRET_KEY = secrets.get_secret('SECRET_KEY')
  
  # Application definition
  
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
  
  ROOT_URLCONF = 'pracpjt2.urls'
  
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  
  WSGI_APPLICATION = 'pracpjt2.wsgi.application'
  
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [
          'rest_framework.authentication.TokenAuthentication',
      ]
  }
  
  # Password validation
  # https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
  
  AUTH_PASSWORD_VALIDATORS = [
      {
          'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
      },
  ]
  
  # Internationalization
  # https://docs.djangoproject.com/en/2.1/topics/i18n/
  
  LANGUAGE_CODE = 'ko-kr'
  
  TIME_ZONE = 'Asia/Seoul'
  
  USE_I18N = True
  
  USE_L10N = True
  
  USE_TZ = True
  
  # Static files (CSS, JavaScript, Images)
  # https://docs.djangoproject.com/en/2.1/howto/static-files/
  
  STATIC_URL = '/static/'
  
  # django-allauth
  SITE_ID = 1
  
  # CORS
  CORS_ORIGIN_ALLOW_ALL = True
  
  # Custom User
  AUTH_USER_MODEL = 'accounts.User'
  ```

  - **설정 파일이 기존에 `settings.py`가 있던 위치보다 한 단계 더 낮아졌으므로 `os.path.dirname`을 한 번 더 추가해준다.**
  - `secrets.json`에 git에 저장되지 말아야 할 내용들을 담고 있는데, 추후에 개발 환경과 배포 환경에 따라 다른 파일을 사용할 수 있으므로 클래스로 정의하여 비밀 키값을 들고올 수 있게 하였다.
  - 추후에 로컬 환경과 개발 환경, 배포 환경에 따라 다르게 적용할 사항이 있다면 `local.py`,  `development.py`와 `production.py`로 각각 옮겨서 적용하면 된다.

- **local.py** (로컬)

  ```python
  # settings/local.py
  
  from .base import *
  
  
  DEBUG = True
  
  ALLOWED_HOSTS = []
  
  DATABASES = secrets.get_secret('DATABASES')
  ```

- **development.py** (배포, 협업 개발 환경)

  ```python
  # settings/development.py
  
  from .base import *
  
  
  DEBUG = False
  
  ALLOWED_HOSTS = ['*']
  
  DATABASES = secrets.get_secret('DATABASES')
  ```

- **production.py** (배포, 서비스 환경)

  ```python
  # settings/production.py
  
  from .base import *
  
  
  DEBUG = False
  
  ALLOWED_HOSTS = ['*']
  
  DATABASES = secrets.get_secret('DATABASES')
  ```

  - 로컬 환경과 배포 환경의 `DEBUG`세팅이 다른 것을 볼 수 있다.
  - 현재 `secrets` 변수는 `base.py`에서 가져왔지만, 추후에 다르게 설정할 것이다.

<br>

#### b. 다른 설정으로 실행하기

- 개발 환경과 배포 환경을 분리해뒀으니, 분리된 각 환경설정 대로 실행할 수 있다.

  - `python manage.py runserver --settings={프로젝트이름}.settings.local`이라 하면 로컬 환경으로 설정한 값으로 실행된다.
  - `python manage.py runserver --settings={프로젝트이름}.settings.development`라고 하면 협업 개발 환경으로 설정한 값으로 실행된다.
  - `python manage.py runserver --settings={프로젝트이름}.settings.production`이라 하면 배포 환경으로 설정한 값으로 실행된다.

- 매번 이렇게 명령어를 입력하기 어렵기 때문에 환경변수에 어느 설정을 사용할지 등록해둘 수 있다.

  - 파이썬 가상환경을 만들어 진행했다.
  - `{가상환경 폴더}/Scripts/activate`에 다음 내용을 넣는다. (리눅스 기반 OS라면 `{가상환경 폴더}/bin/activate`를 수정한다.)

  ```
  # venv/Scripts/activate
  
  ...
  export DJANGO_SETTINGS_MODULE={프로젝트 이름}.settings.development
  ...
  ```

  - 이 경우 디폴트를 개발 환경으로 설정하겠다는 의미이다.
  - 이 과정을 거치면 `python manage.py runserver`라고만 입력해도 `python manage.py runserver --settings={프로젝트이름}.settings.development`를 입력했을 때처럼 된다.

<br>

<br>

### 3. secrets.json 분리

- git에 올리지 않으려는 정보(데이터베이스 비밀번호, django SECRET_KEY 등)를 별도로 `secrets.json`이라는 파일에 담아 보관한다.

- 이 또한 django 세팅에 영향을 주므로 개발 환경과 배포 환경에 맞게 따로 관리할 수 있다.

- 이번엔 `secrets-base.json`, `secrets-dev.json`, `secrets-prod.json`으로 나누어보도록 한다.

  ```json
  // secrets-base.json
  
  {
      "SECRET_KEY": "{여기에는 django SECRET_KEY 값이 들어간다}"
  }
  ```

  ```json
  // secrets-local.json
  
  {
      "DATABASES": {
          "default": {
              "ENGINE": "django.db.backends.mysql",
              "NAME": "testdb_local",
              "USER": "root",
              "PASSWORD": "{비밀번호}",
              "HOST": "127.0.0.1",
              "PORT": "3306"
          }
      }
  }
  ```

  ```json
  // secrets-dev.json
  
  {
      "DATABASES": {
          "default": {
              "ENGINE": "django.db.backends.mysql",
              "NAME": "testdb_dev",
              "USER": "root",
              "PASSWORD": "{비밀번호}",
              "HOST": "127.0.0.1",
              "PORT": "3306"
          }
      }
  }
  ```

  ```json
  // secrets-prod.json
  
  {
      "DATABASES": {
          "default": {
              "ENGINE": "django.db.backends.mysql",
              "NAME": "testdb_prod",
              "USER": "root",
              "PASSWORD": "{비밀번호}",
              "HOST": "127.0.0.1",
              "PORT": "3306"
          }
      }
  }
  ```

  - `secrets-base.json`에는 `base.py`에서 사용할 값을 적어두었다.
  - 개발 환경과 배포 환경에서 데이터베이스를 분리해두었다.
  - secret json파일들을 만들어둔 다음엔 커밋하기 전에 반드시 `.gitignore`에 등록한다.

  ```
  # .gitignore
  
  ...
  # secret setting keys
  secrets*.json
  ...
  ```

- `settings/base.py`, `settings/local.py`, `settings/development.py`, `settings/production.py`도 각각의 json파일을 사용한다.

  ```python
  # settings/base.py
  
  ...
  secret_file = os.path.join(BASE_DIR, 'secrets-base.json')
  secrets = Secrets(secret_file)
  ...
  ```

  ```python
  # settings/local.py
  
  from .base import *
  
  
  secret_file = os.path.join(BASE_DIR, 'secrets-local.json')
  secrets = Secrets(secret_file)
  
  DEBUG = True
  
  ALLOWED_HOSTS = []
  
  DATABASES = secrets.get_secret('DATABASES')
  ```

  ```python
  # settings/development.py
  
  from .base import *
  
  
  secret_file = os.path.join(BASE_DIR, 'secrets-dev.json')
  secrets = Secrets(secret_file)
  
  DEBUG = False
  
  ALLOWED_HOSTS = ['*']
  
  DATABASES = secrets.get_secret('DATABASES')
  ```

  ```python
  # settings/production.py
  
  from .base import *
  
  
  secret_file = os.path.join(BASE_DIR, 'secrets-prod.json')
  secrets = Secrets(secret_file)
  
  DEBUG = False
  
  ALLOWED_HOSTS = ['*']
  
  DATABASES = secrets.get_secret('DATABASES')
  ```
  
  - 이제 더이상 `local.py`, `development.py`와 `production.py`에서 `base.py`로 부터 가져온 `secrets`를 쓰지 않고 각각의 json파일을 사용하여 새로 정의해서 사용하는 것을 볼 수 있다.

<br>

<br>

<br>

<br>

참고자료

- [Jihun's Development Blog](https://cjh5414.github.io/django-settings-separate/)
- [끄적끄적 cODe](https://ehfgk78.github.io/2018/02/02/Django-Settings_Requirements/)