### 1. Amazon EC2 인스턴스 만들기

- 설정
  - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.html
- 시작하기
  - https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/EC2_GetStarted.html



### 2. git 설정 및 settings.py 나누기

- mysql도 연동
- & 테스트
- ubuntu에 git 설치
  - sudo apt-get update
  - sudo apt-get install -y vim git wget



### 3. django (& mysql) docker 구성

- **https://docs.docker.com/compose/django/**



- ERROR: Named volume "db-data:/var/lib/mysql:rw" is used in service "db" but no declaration was found in the volumes section. 에러날 때 대처법
  - `volumes:` 를 추가해준다.
    https://azizkhani.github.io/2017-08-24-docker-but-no-declaration-was-found-in-the-volumes/

- django.db.utils.OperationalError: (2002, "Can't connect to MySQL server on 'db' (115)")

  - https://stackoverflow.com/questions/57407940/cant-connect-to-mysql-while-building-docker-compose-image

- django.db.utils.OperationalError: (1045, 'Plugin caching_sha2_password could not be loaded: /usr/lib/x86_64-linux-gnu/mariadb19/plugin/caching_sha2_password.so: cannot open shared object file: No such file or directory')

  - 이유일 수 있는 것: MySQL 8.0부터 강화된 password 체계 때문에 - https://ondemand.tistory.com/246
  - https://collinsd.tistory.com/294 

- ```
  This could be because you hit a bug. It is also possible that this binary
  mysql_1                | or one of the libraries it was linked against is corrupt, improperly built,
  mysql_1                | or misconfigured. This error can also be caused by malfunctioning hardware.
  mysql_1                | Attempting to collect some information that could help diagnose the problem.
  mysql_1                | As this is a crash and something is definitely wrong, the information
  mysql_1                | collection process might fail.
  mysql_1                | 
  mysql_1                | key_buffer_size=8388608
  mysql_1                | read_buffer_size=131072
  ```

  - 차지하는 buffer가 너무 커서 생기는 듯하다. 많이 만들어둔 걸 지우고 다시 up해보자.
  - https://github.com/laradock/laradock/issues/1173



- Docker image push
  - https://galid1.tistory.com/324



- Dockerfile

  ```dockerfile
  FROM python:3.7.6
  ENV PYTHONUNBUFFERED 1
  RUN mkdir /code
  WORKDIR /code
  COPY requirements.txt /code/
  RUN pip install -r requirements.txt
  COPY . /code/
  ```

  

- docker-compose.yml

  ```yml
  version: '3'
      
  services:
      db:
          image: mysql:5.7
          volumes:
              - db_data:/var/lib/mysql
          environment:
              MYSQL_ROOT_PASSWORD: ssafy
              MYSQL_DATABASE: deploytest-local
          command: 
              - --character-set-server=utf8mb4
              - --collation-server=utf8mb4_general_ci
          ports:
              - "7000:3306"
      web:
          build: .
          command: python manage.py runserver 0.0.0.0:8000 --settings=djangodeploy.settings.local
          volumes:
              - .:/code
          ports:
              - "8000:8000"
          depends_on:
              - db
  
  volumes:
      db_data:
  ```



#### Dockerfile이 다른 곳에 있다면

```dockerfile
services:
  nginx:
  build:
    context: /mnt/backup			## Dockerfile이 있는 경로 (절대경로 또는 상대경로)
    dockerfile: Dockerfile-agent    ## 파일명이 Dockerfile이 아닐 경우 파일명 기입
```

- https://nirsa.tistory.com/79
- 아니면 그냥 build 부분에서 경로를 입력해줘도 된다.




#### volume 데이터 저장 위치

- /var/lib/**docker**/**volumes**/{volume_name}
- `docker volume ls`로 볼륨 목록을 살펴보고 `docker volume inspect {볼륨 이름}`으로 `Mountpoint`를 살펴봐도 볼 수 있다.



#### docker container 안에 있는 mysql에 접속

- https://velog.io/@wimes/Docker%EB%A1%9C-MySQL-%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88-%EB%A7%8C%EB%93%A4%EA%B8%B0
- 컨테이너의 세부 정보를 inspect 명령어로 알아낸 다음 접속한다.
  - ipaddress가 없을 수도 있는데, 이건 `--net host` 옵션으로 실행되고 있기 때문이다. host IP에 접근하면 된다.
  - https://stackoverflow.com/questions/43803849/my-docker-container-does-not-have-ip-address-why

- docker network: https://www.daleseo.com/docker-compose-networks/



- lost connection to mysql server at 'reading initial communication packet' system error 0
  - 맞는 포트번호를 입력한다.
  - **외부에서 (ex. workbench) container 내부의 mysql로 진입할 때는 container의 port번호로 연결해야 한다!!!!!!**
  - **이미 쓰고있는 포트로는 동시에 다른 컨테이너를 열 수 없다**



#### 테이블 만들어주기

- migrate 해서 테이블 만들어준다.
- 이미 docker-compose up --build 해서 db 만들어지고 나면 다시 안 만들어지는 경우가 있다.
  - 접속해서 수동으로 해당 db 만들어줘도 괜찮다.



- docker-compose.yml

  ```yml
  version: '3'
      
  services:
      db:
          image: mysql:5.7
          volumes:
              - db_data:/var/lib/mysql
          environment:
              MYSQL_ROOT_PASSWORD: ssafy
              MYSQL_DATABASE: deploytest-dev
          command: 
              - --character-set-server=utf8mb4
              - --collation-server=utf8mb4_general_ci
          ports:
              - "7000:3306"
      web:
          build: .
          command: python manage.py runserver 0.0.0.0:8000 --settings=djangodeploy.settings.local
          volumes:
              - .:/code
          ports:
              - "8000:8000"
          depends_on:
              - migration
      migration:
          build: .
          command: python manage.py migrate --settings=djangodeploy.settings.development
          volumes:
              - .:/code
          links:
              - db
          depends_on:
              - db
  
  volumes:
      db_data:
  ```

  - https://stackoverflow.com/questions/30063907/using-docker-compose-how-to-execute-multiple-commands



#### * Logging sample

```python
import os
from datetime import date

...

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        },
    },
    'handlers': {
        # this is what you see in runserver console
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        # this handler logs to file
        #▼▼▼▼ this is just a name so loggers can reference it
        'file': {  
            'class': 'logging.FileHandler',
            #  choose file location of your liking
            'filename': os.path.join(os.path.join(os.path.dirname(BASE_DIR), 'django-dev-log'), f'{date.today().isoformat()}-django.log'),  
            'formatter': 'standard'
        },
    },
    'loggers': {
        # django logger
        'django': {
            # log to console and file handlers
            'handlers': ['console', 'file'],  
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),  # choose verbosity
        },
    },
}
```

- docker를 활용하여 log를 만들 때엔 Dockerfile에 log가 저장되는 폴더도 만들어주는 명령어를 넣어야 한다.

  - Dockerfile

    ```dockerfile
    FROM python:3.7.6
    ENV PYTHONUNBUFFERED 1
    RUN mkdir /code
    WORKDIR /code
    RUN mkdir -p /django-dev-log
    COPY requirements.txt /code/
    RUN pip install -r requirements.txt
    COPY . /code/
    ```

- container 안의 내용을 보고싶으면 `docker exec -it [container ID] /bin/bash`로 들어가볼 수 있다.
  - cp 명령어로 host로 복사해올 수도 있다.
  - `docker cp <containerId>:/file/path/within/container /host/path/target`
    - https://stackoverflow.com/questions/22049212/copying-files-from-docker-container-to-host
  
- 로그 파일 저장시 `PermissionError: [WinError 32] 다른 프로세스가 파일을 사용 중이기 때문에 프로세스가 액세스 할 수 없습니다:` 에러 뜨는 경우

  - 웹 서버 기동 옵션에 --noreload를 설정하여 기동하도록 한다.
  - https://yscho03.tistory.com/3

- logging HTTPHandler 로그 커스텀 

  - https://hwangheek.github.io/2019/python-logging/
  - https://stackoverflow.com/questions/62957814/python-logging-log-data-to-server-using-the-logging-module
  - https://stackoverflow.com/questions/34886267/retrieving-the-request-object-in-a-custom-django-logging-handler






### 4. Ubuntu에서 docker 확인

- ERROR: Couldn't connect to Docker daemon at http+docker://localunixsocket - is it running?

  - sudo로 가동해보기.

  

- 웹서버 없이 애플리케이션에 접근하고 싶으면 인바운드 규칙을 설정해줘야 한다.
  
  - https://victorydntmd.tistory.com/338





### 5. gunicorn docker 구성

- gunicorn은 ubuntu 환경에서 작동하는지 확인하기.
  - ModuleNotFoundError: No module named 'fcntl' : 윈도우에서 모듈 못쓴다.
    - https://stackoverflow.com/questions/45228395/error-no-module-named-fcntl



- docker-compose.yml

  ```yml
  version: '3'
      
  services:
      db:
          image: mysql:5.7
          volumes:
              - db_data:/var/lib/mysql
          environment:
              MYSQL_ROOT_PASSWORD: ssafy
              MYSQL_DATABASE: deploytest-dev
          command: 
              - --character-set-server=utf8mb4
              - --collation-server=utf8mb4_general_ci
          ports:
              - "7000:3306"
      web:
          build: .
          command: gunicorn --env DJANGO_SETTINGS_MODULE=djangodeploy.settings.development --bind 0.0.0.0:8000 djangodeploy.wsgi:application
          volumes:
              - .:/code
          ports:
              - "8000:8000"
          depends_on:
              - migration
      migration:
          build: .
          command: python manage.py migrate --settings=djangodeploy.settings.development
          volumes:
              - .:/code
          links:
              - db
          depends_on:
              - db
  
  volumes:
      db_data:
  ```



- **debug를 True로 하더라도 swagger가 나오지 않는다.**
  - **개발용 서버는 runserver로 만드는 게 좋을 것 같다.**



### 6. nginx docker 구성

- proxy/nginx.conf 를 만들어서 사용할 수 있을 것
  
  - 리버스 프록시 구성: https://medium.com/sjk5766/docker-compose%EB%A1%9C-localhost-nginx-%EB%A6%AC%EB%B2%84%EC%8A%A4-%ED%94%84%EB%A1%9D%EC%8B%9C-%EA%B5%AC%EC%84%B1-8214d41a94fc
- docker hub에서 설명하는 nginx image 사용법
  
- https://hub.docker.com/_/nginx
  
- spring-boot, mysql, nginx를 docker-compose로 띄우기 (원리가 비슷하다.)

  >  nginx는 `/etc/nginx/conf.d` 내에 들어있는 모든 `.conf` 파일을 include 한다

  - https://joont92.github.io/docker/docker-compose%EB%A1%9C-nginx-spring-boot-mysql-%EA%B5%AC%EC%84%B1%ED%95%98%EA%B8%B0/



#### jenkins랑 같이 쓰려다보니 nginx docker 포기 -_-



`/etc/nginx/sites-available`에 conf 파일 만들고 심볼릭 링크로 `/etc/nginx/sites-enabled`에 연결.

- childrenzip.conf

  ```nginx
  server {
  
          listen  80;
          listen [::]:80;
          server_name childrenzip.site;
  
  
          location / {
                  root /home/ubuntu/dist; 
                  index index.html;
                  try_files $uri $uri/ /index.html;
          }
      
          location /media {
              	alias /home/ubuntu/media; 
          }    
      
  	    location ^~ /.well-known/acme-challenge/ {
  				default_type "text/plain";
  				root     /usr/share/nginx/html;
  		}    # for https
  
          location /api {
                  proxy_pass http://localhost:8800;
                  proxy_redirect off;
                  charset utf-8;
                  proxy_set_header X-Real_IP $remote_addr;
                  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                  proxy_set_header X-Forwarded-Proto $scheme;
                  proxy_set_header X-NginX-Proxy true;
          }
  }
  
  server {
          listen 80;
          listen [::]:80;
          server_name www.childrenzip.site;
  
          location / {
                  return 301 http://childrenzip.site$request_uri;
          }
  }
  ```

  - 8800는 web container가 expose해놓은 포트번호이다.
  - `/home/ubuntu/dist`는 젠킨스 빌드되고 나서 `publish over ssh`를 통해 전송받은 내용이 담겨있다. (dist 파일을 옮겼다.)

- 심볼릭 링크 거는법

  ```
  cd sites-enabled
  sudo ln -s ../sites-available/foo.conf .
  ls -l
  ```

  - ls -l 은 확인하는 작업이다.



- 다음번에 nginx docker-compose
  - docker-compose volume의 뒷쪽을 바꿔서 한번 파일이 가는지 확인부터 해보도록.



- https 적용한 configure.

  ```nginx
  server {
  
          listen  443;
          listen [::]:443;
          server_name childrenzip.site;
      
      
      	ssl on; 
      	ssl_certificate /etc/letsencrypt/live/childrenzip.site/fullchain.pem; 
      	ssl_certificate_key /etc/letsencrypt/live/childrenzip.site/privkey.pem; 
      	ssl_session_timeout 5m; 
  	    # ssl_protocols SSLv2 SSLv3 TLSv1;
      	ssl_protocols TLSv1.1 TLSv1.2 TLSv1.3;
      	# ssl_ciphers HIGH:!aNULL:!MD5;
      	ssl_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH';
      	ssl_prefer_server_ciphers on;
  
  
  
          location / {
                  root /home/ubuntu/dist; 
                  index index.html;
                  try_files $uri $uri/ /index.html;
          }
      
          location /media {
              	alias /home/ubuntu/media; 
          }    
      
  	    location ~ /\.ht {
  	        	deny  all;
      	}
      
      	location /api {
                  proxy_pass http://localhost:8000;
                  proxy_redirect off;
                  charset utf-8;
                  proxy_set_header X-Real_IP $remote_addr;
                  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                  proxy_set_header X-Forwarded-Proto $scheme;
                  proxy_set_header X-NginX-Proxy true;
          }
  }
  
  server {
          listen  80;
          listen [::]:80;
          server_name childrenzip.site;
      
          location / {
                  return 301 https://childrenzip.site$request_uri;
          }
      
  	    location ^~ /.well-known/acme-challenge/ {
  				default_type "text/plain";
  				root     /usr/share/nginx/html;
  		}    # for https
      
  }
  
  server {
          listen 80;
          listen [::]:80;
          server_name www.childrenzip.site;
  
          location / {
                  return 301 https://childrenzip.site$request_uri;
          }
  }
  ```

  
  



### 7. jenkins docker 구성

- pdf파일 ssafy에서 받은거 참고

  - 포트번호를 8080으로 해야한다. (기본 이미지에 그런 식으로 설정되어있는듯?)

  - getting started에서 X가 뜨는 것들이 생겨있다. (build timeout, credentials binding, timestamper 등등)

    ![image-20200925165901670](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20200925165901670.png)

  - retry  해도 똑같이 다 안되니까 그냥 continue 눌러서 넘어갔다.

    - 소켓만 연결해줬는데도 되는게 엄청 많아진다..?
    - 그다음 유저 적는건 skip, 그다음은 host:8080로 save and finish했다.
    - 유저는 만드는게 좋을듯.
    - 유저 안 만들고 다시 들어가려면 아이디는 `admin`으로 하고 docker container 내부의 `/var/jenkins_home/secrets/initialAdminPassword` 경로에 있는 비밀번호를 입력해서 로그인 할 수 있다. (로그로도 비밀번호를 알 수 있다. (`docker logs {docker 해시값}`))
    - ssh연결로 해본다.
      https://m.blog.naver.com/PostView.nhn?blogId=baekmg1988&logNo=221658364543&categoryNo=72&proxyReferer=https:%2F%2Fwww.google.com%2F
    - https://marindie.github.io/jenkins/Jenkins-Gitlab-KR/#toc2 username - password 입력하니까 에러메시지 없어짐 (소스코드 관리에서 git 선택할때)

- https://www.hanumoka.net/2019/10/13/docker-20191013-docker-compose-ubuntu-jenkins/ 참고

- https://medium.com/@pks2974/jenkins-%EC%99%80-docker-%EA%B7%B8%EB%A6%AC%EA%B3%A0-aws-cli-%EC%82%BD%EC%A7%88%EA%B8%B0-%EC%A0%95%EB%A6%AC%ED%95%98%EA%B8%B0-e728986960e2 참고



**jenkins 컨테이너를 사용해서 docker 컨테이너 프로젝트를 구동하는 방식으로 이해해야 할 듯 하다.**

- https://www.youtube.com/watch?v=BUg2kDfhsks&list=PLRx0vPvlEmdChjc6N3JnLaX-Gihh5pHcx&index=10
- 구조: https://www.hanumoka.net/2019/10/14/docker-20191014-docker-jenkins-docker-in-docker/
  https://tutorials.releaseworksacademy.com/learn/the-simple-way-to-run-docker-in-docker-for-ci
- `docker run -d -p 8080:8080 -v ~/jenkins-dev:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --name jenkins_dev -u root jenkins/jenkins:lts`

- `secrets` 파일들도 가져오려면 jenkins를 위한 Dockerfile을 따로 만든 다음에 사용해야할듯 싶은데..
  - 우선 파일 복사해오는 방법은 `docker cp foo.txt mycontainer:/foo.txt`처럼 하면 된다.
    https://stackoverflow.com/questions/22907231/copying-files-from-host-to-docker-container
    - 파일 복사해주는 .sh 만들어서 수행중.



secret 파일도 넣어서 구동하려고 하면

1. jenkins image를 받아서 docker run한다.

2. jeckins 설정을 마치고 run해서 pull받아온다.

3. secret파일을 workspace에 맞는 폴더에 각각 넣는다.

4. build 명령어 입력해서 CI/CD 설정한다.

   - docker compose build step 이라는 플러그인을 설치한다. (for docker-compose)

     - 플러그인이 빌드를 못하는거같아서 docker를 그냥 설치하고 compose하는게 나을수도 있겠다 생각든다 (shell에서 실행해서) (**플러그인 설치 안하고 하는거**)
     - docker-compose 설치하도록 shell script에 입력함.

   - nodejs 플러그인을 설치한다 (for npm) & global tool configurations에서 설정.

     - c/c++컴파일러를 못찾아서 에러 날 수 있다. - `apt-get install g++ build-essential` 추가
       https://stackoverflow.com/questions/57156171/problem-running-npm-install-in-jenkins-pipeline

```
     apt-get install g++ build-essential
     cd frontend
     npm install
     npm run build
     npm run generate
```



jenkins docker 빌드중에 No such file or directory 에러뜰때

- docker installation 설정을 해주었다.
- https://stackoverflow.com/questions/50333325/jenkins-cannot-run-program-docker-error-2-no-such-file-or-directory
- volume 설정을 절대 경로 말고 docker에 맞게 설정해줬을 때 (ex. db_data처럼) 정상적으로 빌드되었다.
  - 데이터는 `/var/lib/docker/volumes/{폴더이름}`에 저장 되어있다.



jenkins 빌드 후에 mattermost webhook 사용할 때

- jenkins 관리 -> 플러그인 관리 -> 고급에서 no proxy host에 웹훅 url 제출한다. (플러그인은 http를 사용하기 때문)



volume 파일 임의로 지워서 Cannot create container for service migration 에러날 때

- `docker volume ls` 명령어로 volume을 보고, 원하는 걸 지운다. (`docker volume rm {지울 volume}`)
- https://stackoverflow.com/questions/51817245/docker-error-cannot-create-container-for-service-no-such-file-or-dir



--force-recreate, --renew-anon-volumes 옵션으로 이전 컨테이너에서 데이터를 받아오지 않게 할 수 있다.

- 이거도 그냥 cache를 안쓰고 다시 container 만드는거라 이미 만들어진 container를 지우고 나서야 원하는 대로 작동한다.

force push는 반영이 안되나..?

- 그건 아닌거같고 빌드할때마다 바뀐 거로 적용이 안되는것같다.

- 해결책: ~~CI를 할 땐 `docker-compose rm -f` 옵션을 준 다음 빌드하는게 나은듯.~~

  - https://stackoverflow.com/questions/32612650/how-to-get-docker-compose-to-always-re-create-containers-from-fresh-images

  - 그런데 db까지 모두 삭제하면 안될듯하다. **docker volume 삭제로 web, migrations만 없애면 작동함!**

    - *애초에 volume으로 웹을 만들어놓지 않더라도 가능할 거 같긴 하다.*

  - jenkins docker 내부에 docker를 깔아야할듯하다.

    - ~~docker plugin을 깐다면? 안 된다~~

    - 도커를 직접 jenkins container 내부에 설치해보자.

      - package로 설치해야 되는듯 (repository 설정해서 하는 방식은 에러생김)
  
      1. package를 선택한다. (우분투 버전, 커널에 맞춰서) -> 선택하면 pool/stable로 간다
         - containerd.io, docker-ce-cli, docker-ce가 있는데 jenkins container 안에서 daemon을 조정할 목적으로 설치하는 것이므로 **docker-ce-cli**를 깔아보자.
         - 근데... jenkins container 안에서는 debian으로 설치된 것 같다..!
         - https://www.reddit.com/r/docker/comments/dsr6y2/containerdio_vs_dockercecli_vs_dockerce_what_are/
         - 패키지를 설치한 다음에 jenkins container 내부로 옮긴 다음 설치하자.
           `docker cp /host/path/target <containerId>:/file/path/within/container`
      2. dpkg로 설치한다.



#### jenkins execute shell command

- dev

```
cd backend
docker stop backend-dev
docker rm backend-dev backend_migration_1
docker volume rm -f backend_web_dev backend_migration_1
docker rmi backend_web backend_migration
docker-compose up -d --force-recreate --renew-anon-volumes
```



- prod

```
cd frontend
npm install
npm run build
npm run generate
```

```
docker stop backend-prod 
docker rm backend-prod childrenzip-prod_migration_1
docker volume rm -f childrenzip-prod_web_prod childrenzip-prod_migration
docker rmi childrenzip-prod_web childrenzip-prod_migration
docker-compose up -d --force-recreate --renew-anon-volumes
```

- docker-compose up을 매번 하면 환경 변화에 대응하기는 괜찮을듯.
- docker exec으로 변화된 부분만 바꿔 적용하는 것도 생각해볼만 하다.



#### copy_files_dev.sh -> jenkins container에 실행하는 명령

- jenkins container에서 사용할 패키지 설치용
- git pull 한번 받고나서 secret파일 옮기는 용도

```bash
#!/bin/sh

CONTAINER_NAME="jenkins_dev"
WORKSPACE="/var/jenkins_home/workspace/childrenzip-dev/backend"

sudo docker exec $CONTAINER_NAME bash -c "apt-get update" 
sudo docker exec $CONTAINER_NAME bash -c "apt-get install -y build-essential" 

# docker
sudo docker cp docker-ce-cli_19.03.6_3-0_debian-stretch_amd64.deb $CONTAINER_NAME:/home
sudo docker exec $CONTAINER_NAME bash -c "dpkg -i /home/docker-ce-cli_19.03.6_3-0_debian-stretch_amd64.deb"

# docker compose
sudo docker exec $CONTAINER_NAME bash -c 'curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose'
sudo docker exec $CONTAINER_NAME bash -c 'chmod +x /usr/local/bin/docker-compose'

# copy secret files
cd childrenzip-dev/backend
sudo docker cp docker-compose.yml $CONTAINER_NAME:$WORKSPACE/docker-compose.yml
sudo docker cp secrets-base.json $CONTAINER_NAME:$WORKSPACE/secrets-base.json
sudo docker cp secrets-dev.json $CONTAINER_NAME:$WORKSPACE/secrets-dev.json
```

- 근데 dev copy는 안해도 Dockerfile에서 해준 거 아닌가..?



- 빌드후에 dist폴더로 보내고, nginx 컨테이너에 다시 올려주기 위해 publish over ssh에서
  - exec command로 `docker cp`를 사용하여 dist폴더를 nginx 컨테이너의 /home으로 보내주었다.
  - `sudo docker cp ~/dist childrenzip-prod_nginx_1:/home`



- nginx conf 복사 - dockerfile 만들어서 진행



- jenkins container는 하나만 띄우고 여기에 개발, 배포환경 각각 배포되게끔 해도 될거같은데.
  - 일단 지금은 각각 띄워보자 (jenkins container이름도 dev, prod로 나눠둠)





### * EC2 환경에 설치해야 할 것

- git
- docker, docker-compose



#### ubuntu 버전확인 및 커널 확인

- ubuntu 버전확인: `lsb_release -a`
- 커널 확인: `uname -a`
- 우분투 릴리즈별 코드명: https://wiki.ubuntu-kr.org/index.php/%EC%9A%B0%EB%B6%84%ED%88%AC_%EB%A6%B4%EB%A6%AC%EC%A6%88%EB%B3%84_%EC%BD%94%EB%93%9C%EB%AA%85
  - 18.04: bionic beaver
  - 16.04: xenial xerus
  - x86_64는 AMD64로 보고 진행하면 될듯..?



#### debian 릴리즈별 코드명

- https://www.debian.org/releases/
- 데비안 10 - buster // 9 - stretch // 8 - jessie // 7 - wheezy





### 구조

- 모두 도커 컨테이너에 띄우려고 하니까 쉽지 않다.

1. jenkins container를 실행한다. (socket 연결)

2. jenkins 빌드되면 (git pull 받아오면) secret 파일들을 모두 ec2로 옮겨서 shell script로 한번에 원하는 곳으로 다 옮긴다.

   - 개발 관련 도커는 사용해도 될듯하다.

   - publish over ssh로 호스트 서버에 빌드된 프론트 파일을 옮긴다.

3. nginx로 원하는 포트로 연결시킨다.





#### 최종 docker-compose

- dev

  ```yml
  version: '3'
      
  services:
      db:
          image: mysql:5.7
          volumes:
              - db_data:/var/lib/mysql
          environment:
              MYSQL_ROOT_PASSWORD: ssafy
              MYSQL_DATABASE: childrenzip-dev
          command: 
              - --character-set-server=utf8mb4
              - --collation-server=utf8mb4_general_ci
          ports:
              - "7000:3306"
      web:
          build: .
          container_name: backend-dev
          command: python manage.py runserver 0.0.0.0:8800 --settings=spc_pjt.settings.development --noreload
          volumes:
              - web_dev:/code
              - dev_log:/django-dev-log
              - media_dev:/code/media
          ports:
              - "8800:8800"
          depends_on:
              - migration
      migration:
          build: .
          command: python manage.py migrate --settings=spc_pjt.settings.development
          volumes:
              - web_dev:/code
              - dev_log:/django-dev-log
          links:
              - db
          depends_on:
              - db
  
  volumes:
      db_data:
      web_dev:
      dev_log:
      media_dev:
  ```

  

- prod

  ```yml
  version: '3'
      
  services:
      db:
          image: mysql:5.7
          volumes:
              - db_data:/var/lib/mysql
          environment:
              MYSQL_ROOT_PASSWORD: ssafy
              MYSQL_DATABASE: childrenzip-prod
          command: 
              - --character-set-server=utf8mb4
              - --collation-server=utf8mb4_general_ci
          ports:
              - "8500:3306"
      web:
          build: ./backend
          container_name: backend-prod
          command: gunicorn --env DJANGO_SETTINGS_MODULE=spc_pjt.settings.production --bind 0.0.0.0:8000 spc_pjt.wsgi:application
          volumes:
              - web_prod:/code
              - prod_log:/django-prod-log
              - media_prod:/code/media
          ports:
              - "8000:8000"
          depends_on:
              - migration
      migration:
          build: ./backend
          command: python manage.py migrate --settings=spc_pjt.settings.production
          volumes:
              - web_prod:/code
              - prod_log:/django-prod-log
          links:
              - db
          depends_on:
              - db
  
  volumes:
      db_data:
      web_prod:
      prod_log:
      media_prod:
  ```

  

