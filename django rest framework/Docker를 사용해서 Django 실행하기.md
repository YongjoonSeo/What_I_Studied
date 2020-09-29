## Docker를 사용해서 Django 실행하기

### 1. Docker container 만들기

#### a. Dockerfile 구성하기

- Dockerfile은 image로 container를 어떻게 구성할 것인지 적혀있는 문서이다.

  ```dockerfile
  FROM python:3.7.6
  
  RUN apt-get update \
      && apt-get install -y --no-install-recommends
  
  COPY . /app  # 나의 Django 코드를 컨테이너에 복사합니다.
  RUN pip install -r /app/requirements.txt  # requirements.txt에 적혀있는 pip 패키지들을 설치합니다.
  RUN chmod 755 /app/start  # start 파일을 실행 가능하게 합니다.
  WORKDIR /app  # 워킹디렉토리를 /app으로 합니다.
  EXPOSE 8000  # 8000번 포트를 expose합니다.
  
  ENTRYPOINT ["/app/start"]  # /app/start 파일을 실행시킵니다.
  ```

  - `-y` 옵션은 설치에 동의하는지 물을 때 yes(-y)라고 응답한다는 의미이다.
  - `--no-install-recommends`옵션은 필요한 패키지들만 설치한다는 의미이다.
  - `ENTRYPOINT`의 가장 마지막 지시만 효과가 있기 때문에, 여러 줄의 명령어를 실행하기 위해 `start`라는 파일에 명령어를 저장해두었다.

  ```
  # start
  
  python manage.py makemigrations
  python manage.py migrate
  
  python manage.py runserver 0.0.0.0:8000
  ```

  - `0.0.0.0:8000`은 모든 IP에서 8000번 포트로 접근 가능하다는 의미이다.

- `docker build -t django .` 명령어로 docker image를 빌드한다.

  - `-t django` 부분은 이미지에 `django`라는 이름을 붙인다는 의미이다.
  - `.`은 현재 디렉토리에서 docker image 빌드를 시작한다는 의미이다.







참고자료

- [Docker docs](https://docs.docker.com/)
- [Siner's DevLog](https://siner308.github.io/2019/02/25/django-docker-custom-image/)
- [new_challenge](https://soyoung-new-challenge.tistory.com/74)
- [서비큐라 기술 블로그](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html)