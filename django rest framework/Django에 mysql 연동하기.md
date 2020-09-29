## Django에 mysql 연동하기

### 1. mysql에서 데이터베이스 생성

- MySQL Workbench를 사용하여 진행하면 편하다.
- 먼저 connection을 하나 만들도록 하자. 여기서 `Hostname`, `Port`, `Username`, `Password`를 기억하자.

![workbench1](https://i.ibb.co/GMdXtx6/workbench1.jpg)

- 그다음 데이터베이스를 하나 만들자.
- Charset은 `utf8mb4`, Collation은 `utf8mb4_0900_ai_ci`로 설정했다.
  - 이모티콘도 사용하기 위해서는 `utf8mb4` Charset을 써야한다.
  - `utf8mb4_general_ci`와 `utf8mb4_general_ci`보다 `utf8mb4_0900_ai_ci`를 쓰는 걸 권장한다.
    - `utf8mb4_0900_ai_ci`가 가장 최근 UCA 버전(9.0.0)을 사용하고 있다. [Collation 참고](https://dev.mysql.com/doc/refman/8.0/en/charset-collation-names.html)

![workbench2](https://i.ibb.co/N6CqQvv/workbench2.jpg)

- 이때 `Name`부분을 무엇으로 했는지 기억해두자.

![workbench3](https://i.ibb.co/X2qQkHH/workbench3.jpg)

- Apply 버튼을 누르면 데이터베이스가 생성된다.
  - 생성 결과: ![workbench4](https://i.ibb.co/Sd2JfBR/workbench4.jpg)

<br>

<br>

### 2. django에 mysql 설정

#### a. MySQL DB API 드라이버 설치

- MySQL DB API 드라이버에는 `mysqlclient`나 `MySQL Connector/Python`과 같은 것들이 있다.
  - django 공식 문서에서는 `mysqlclient`를 권장하고 있다.
  - django에서 `mysqlclient` 버전은 1.4.0 이상이 필요하다.
- `pip install mysqlclient` 명령어를 통해 `mysqlclient`를 설치한다.
  - 새로운 패키지를 설치했으면 `pip freeze > requirements.txt` 명령어를 통해 패키지 리스트를 올려두자.

<br>

#### b. django 데이터베이스 설정 변경

- 데이터베이스 관련 설정은 git에 올리지 말아야 한다.

- `my_settings.py`라는 파일을 별도로 만들어 관리하자.

  - **반드시 `.gitignore`에 등록하자.**
  - `secrets.json`과 같은 json파일을 만든 후 그곳에 저장해서 관리해도 된다.

  ```
  # .gitignore
  
  ...
  
  # Databases
  my_settings.py
  ```

  ```python
  # my_settings.py
  
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'testdb',
          'USER': 'root',
          'PASSWORD': '{비밀번호}',
          'HOST': '127.0.0.1',
          'PORT': '3306',
      }
  }
  ```

  - MySQL Workbench를 사용하여 데이터베이스를 만들 때 기억해두자 했던 옵션들을 여기 적는다.

- `settings.py`에서 `my_settings.py`를 import 하여 데이터베이스를 설정한다.

  ```python
  # settings.py
  
  from . import my_settings
  ...
  
  # DATABASES = {
  #     'default': {
  #         'ENGINE': 'django.db.backends.sqlite3',
  #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  #     }
  # }
  DATABASES = my_settings.DATABASES
  ```

  - `DATABASES` 주석처리된 부분은 기존 설정이다. 이 부분을 지우고 설정을 바꿔주면 된다.

<br>

#### c. 데이터베이스에 테이블 생성

- 모델 기반으로 schema가 생성되지 않았다면 (즉 각 app마다 `migrations/0001_initial.py`와 같은 파일이 없다면) `python manage.py makemigrations` 명령어를 통해 schema를 만들어준다.

- `python manage.py migrate` 명령어를 통해 데이터베이스에 테이블을 생성한다.

- 실행 결과

  ![workbench5](https://i.ibb.co/qRb2y79/workbench5.jpg)

<br>

<br>

<br>

<br>

참고자료

- [Django Documentation](https://docs.djangoproject.com/en/3.1/)
- [devmin 블로그](https://velog.io/@devmin/Django-MySQL-Connect)
- [Stack overflow](https://stackoverflow.com/questions/766809/whats-the-difference-between-utf8-general-ci-and-utf8-unicode-ci)
- [MySQL Documentation](https://dev.mysql.com/doc/refman/8.0/en/charset-collation-names.html)

