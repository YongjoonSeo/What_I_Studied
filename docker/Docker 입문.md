## Docker 입문

### 1. Docker란?

- Docker는 **container**라 불리는 독립된 환경으로 애플리케이션을 구동할 수 있게 하는 플랫폼이다.
- OS 환경에 따라 하나의 애플리케이션을 사용하려 해도 명령어가 각각 다르다. 불편하다.
  - Docker는 환경에 상관없이 애플리케이션을 같은 방법으로 실행할 수 있게 해준다. (개발 환경을 동일하게 할 수 있다.)
    - 한국에서의 콘센트는 둥그런 모양이고 미국에서는 얇고 납작한 모양을 쓰는 것처럼 같은 전자제품이라도 다양한 나라에서 사용하려면 멀티 어댑터가 필요한 것과 비슷하게 이해할 수 있을 것 같다. (콘센트 모양 - OS, 전자제품 - 애플리케이션, 멀티 어댑터 - Docker)

<br>

<br>

### 2. Docker의 구성요소

- Docker는 크게 image와 container로 구성되어있다.
- 주된 작업 흐름은 **image를 빌드하고, image를 옮기고, image를 실행하는 것이다.**

<br>

#### a. image

- **Docker container를 만들기 위한 읽기 전용 템플릿이다.**
- 종종 다른 이미지를 기반으로 하기도 한다. (예: ubuntu이미지를 기반으로 하지만 아파치 웹서버를 설치하는 것 등.)
 - 이미지를 직접 만들 수도 있고 다른 사람이 registry에 올려둔 이미지를 사용할 수도 있다.
   - 이미지를 직접 만들기 위해서는 `Dockerfile`을 만들어야 한다.
     - `Dockerfile`에는 이미지를 만들고 실행하는 단계가 적혀있다.
      - `Dockerfile`은 이미지 layer를 만든다. (이미지가 층층이 쌓인 구조라 생각하면 편하다.)
      - `Dockerfile`을 바꾸고 이미지를 다시 빌드한다면, 변경된 layer들만 바뀌며 빌드된다.
        - 변경되는 layer들만 바뀌기 때문에 다른 가상화 기술보다 빠르고 가볍게 작업을 처리할 수 있다.
- 하나의 서버에 여러 image를 활용할 수 있다.
  - Ex) nginx image, MySQL image
- `Docker Hub`에서 여러 image를 무료로 pull하여 사용할 수 있다.

<br>

#### b. container

- **실행 가능한 image 객체이다. (러닝 프로세스)**
- Docker API 또는 CLI를 활용하여 container를 생성, 시작, 중지, 이동, 삭제할 수 있다.

<br>

#### c. docker-compose

- **Compose는 여러 개의 docker container를 정의하고 사용하기 위한 도구이다.**
  - Docker image를 많이 실행하면 container가 많이 생긴다. 이렇게 여러 개의 container를 사용하는 애플리케이션을 사용할 때, YAML 파일을 이용하여 한번에 관리할 수 있다.

<br>

<br>

<br>

<br>

참고자료

- [Docker docs](https://docs.docker.com/)
- [서비큐라 기술 블로그](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html)