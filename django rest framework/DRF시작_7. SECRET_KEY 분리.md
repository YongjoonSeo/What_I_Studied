## SECRET_KEY 분리

- django의 `SECRET_KEY`나 데이터베이스의 비밀번호와 같은 건 공개되면 안 된다.
  - 별도의 파일을 만들어서 관리하거나 환경변수를 사용하는 방법으로 `SECRET_KEY`가 공개되지 않도록 한다.
- `git`에 한 번 올라간 커밋은 모두 남아있기 때문에 맨 처음 커밋하기 전에 `SECRET_KEY`를 감춘 상태로 커밋하는 것이 좋다.

<br>

### 1. Json 파일로 관리

#### a. secrets.json 생성

```json
{
    "SECRET_KEY": "{여기에는 django SECRET_KEY 값이 들어간다}"
}
```

- 이름도 마음대로 지어도 되고, 생성 위치도 마음대로 해도 된다. 나중에 `settings.py`에서 참조만 잘하면 된다.
- 여기서는 `manage.py`와 같은 디렉토리에 생성했다.

<br>

#### b. settings.py에서 불러오기

```python
# settings.py

import os, json
from django.core.exceptions import ImproperlyConfigured


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

secret_file = os.path.join(BASE_DIR, 'secrets.json')
with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets.get(setting)
    except:
        error_msg = f'Set the {setting} environment variable'
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret('SECRET_KEY')
```

- `manage.py`가 있는 디렉토리가 `BASE_DIR`이라는 변수에 저장되어 있으므로, 해당 경로를 이용하여 `secrets.json`을 불러온다.
- 추후에 비밀번호와 같은 다른 변수를 저장하고 싶으면 json파일 안에 저장해두고 같은 방법으로 `settings.py`에서 불러와서 쓰면 된다.

<br>

#### c. .gitignore에 secrets.json을 등록

```
# secret setting keys
secrets.json
```

- 커밋하기 전에 반드시 `.gitignore`에 해당 파일을 등록해서 git이 추적하지 못하게 한다.

<br>

<br>

### 2. 환경변수로 관리 (가상환경)

- 가상환경을 만들어서 현재 프로젝트를 진행하고 있기 때문에 가상환경에서 환경변수를 바꿔줘야 한다.
- 가상환경을 만들지 않는 경우 OS에 따라 맞는 방법으로 환경변수를 등록해주면 된다.

#### a. 환경변수 등록

- 가상환경을 사용하여 환경변수를 만드는 경우, 간단하게 하는 방법으로는 `{가상환경폴더}/Scripts/activate`파일에 직접 변수를 쓰는 방법이 있다.
  - linux 계열의 OS를 사용하는 경우 `{가상환경폴더}/bin/activate`의 경로를 가진다.

```
# venv/Scripts/activate (linux 계열인 경우 venv/bin/activate)

...
export SECRET_KEY="{여기에는 django SECRET_KEY 값이 들어간다}"
...
```

- 현재 `venv`라는 이름으로 가상환경을 만든 상태이다.

<br>

#### b. settings.py에서 사용

```python
# settings.py

...
SECRET_KEY = os.environ.get('SECRET_KEY')
...
```

- `activate` 파일에서 `SECRET_KEY`라는 이름으로 export했기 때문에 환경변수를 불러올 때 해당 이름을 키값으로 가져오면 된다.
- **가상환경을 만들어서 쓰는 경우 가상환경 폴더는 웬만하면 `.gitignore`에 등록해서 사용한다.**

<br>

<br>

<br>

<br>

참고자료

- [Django Documentation](https://docs.djangoproject.com/en/3.1/)
- [초보몽키의 개발공부로그](https://wayhome25.github.io/django/2017/07/11/django-settings-secret-key/)