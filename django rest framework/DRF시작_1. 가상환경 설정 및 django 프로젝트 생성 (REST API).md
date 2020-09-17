## 가상환경 설정 및 django 프로젝트 생성 (REST API)

### 1. 가상환경 생성 및 실행

#### a. 가상환경 만들기

- 프로젝트를 여러 개 진행하면 각각의 프로젝트에서 사용하는 패키지들끼리 충돌이 날 수 있다.

  - 프로젝트 마다 독립적인 환경을 만들어준다.

- 원하는 폴더에서 다음 명령어를 실행한다.

  ```
  python -m venv venv
  ```

  - venv(뒤에 있는 venv)라는 이름으로 가상환경(virtualenv)를 생성한다

<br>

#### b. 가상환경 실행

- 가상환경 폴더(venv)가 만들어진 디렉토리에서 다음 명령어를 실행한다.

  ```
  source venv/Scripts/activate
  # 윈도우 환경
  source venv/bin/activate
  # 리눅스 환경
  ```

- 가상환경 폴더를 생성하고 난 후에는 `.gitignore`를 사용하여 `venv` 폴더가 푸시되지 않도록 하는 게 좋다.

- `pip list` 명령어를 통해 가상환경에 설치된 패키지 리스트를 보면 다음과 같이 나온다.

  ```
  $ pip list
  Package    Version
  ---------- -------
  pip        19.2.3
  setuptools 41.2.0
  ```

<br>

<br>

### 2. django 프로젝트 생성

#### a. django 설치하기

- `pip install django` 명령어로 설치할 수 있다.
  - `pip install django==2.1.15`와 같이 설치할 때 버전을 명시할 수 있다.

<br>

#### b. django 프로젝트 생성

- `django-admin startproject {프로젝트 이름}` 명령어로 django 프로젝트를 만들 수 있다.
  - `django-admin startproject {프로젝트 이름} .`과 같이 `.`을 붙여주면 현재 폴더에 django 프로젝트를 만들 수 있다.
    - 즉, 현재 폴더에 `manage.py` 파일이 생긴다.
- `manage.py`가 있는 디렉토리에서 `python manage.py runserver` 명령어를 통해 서버가 실행되는 것을 볼 수 있다.

<details><summary>django 프로젝트 첫 화면</summary><img src="https://i.ibb.co/yQV6DTq/djangomain.jpg"></details>

<br>

#### c. django rest framework 설치

1. `pip install djangorestframework` 명령어를 통해 django rest framework를 설치한다.

   - django REST API를 만들기 위한 프레임워크이다.

2. `settings.py`의 `INSTALLED_APPS` 변수에 `'rest_framework'`를 추가한다.

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
       'rest_framework'
   ]
   ```