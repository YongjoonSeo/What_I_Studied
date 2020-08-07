# MySQL

1. mysql을 설치하고 접속한다.

   ```
   sudo apt update (패키지 업데이트)
   sudo apt install mysql-server (MySQL 서버 설치)
   sudo mysql -u root -p (MySQL 접속)
   ```

   [(출처: 안경잡이개발자)](https://ndb796.tistory.com/314)

2. database를 만든다. (이후 추가할 spring boot의 application.yml 내용과 일치해야함)

- 한글 깨짐현상 수정

  1. `/etc/mysql/my.cnf` 파일 변경하기 (alternatives에 있으면 해당 파일 변경하면 됨)

  2. 추가해줘야 할 내용

     ```
     [client]
     default-character-set=utf8
     
     [mysql]
     default-character-set=utf8
     
     
     [mysqld]
     collation-server = utf8_unicode_ci
     init-connect='SET NAMES utf8'
     character-set-server = utf8
     ```

  3. MySQL 들어와서 database의 character set을 바꿔준다

     ```mysql
     ALTER DATABASE [DB이름] DEFAULT CHARACTER SET utf8;
     ```

  4. MySQL을 나온 후 `sudo service mysql restart` 명령으로 mysql을 다시 시작한다.

  5. MySQL 들어가서 `status`명령으로 잘 바뀌었는지 확인한다.

  - 이미 만든 데이터베이스가 있는 경우 삭제한 후 스키마를 다시 만들면 utf8이 정상적으로 반영된다.

  [출처: Nesoy Blog](https://nesoy.github.io/articles/2017-05/mysql-UTF8)



# build spring boot

jdk 설치 및 설정 완료한 후

1. git등을 통해 프로젝트를 불러온다.

2. clone한 프로젝트 폴더로 간다.

3. chmod +x gradlew (실행 권한을 설정한다. chmod 777 gradlew도 있는듯)

4. `./gradlew clean build` (빌드한다)

   - Error: Could not find or load main class org.gradle.wrapper.GradleWrapperMain 에러 시

     - gradle wrapper가 누락되어 발생할 수 있다. 다음 명령어를 통해 gradle wrapper를 생성해준다. (시스템에 gradle이 설치되어 있어야 한다.)

       ```
       $ gradle wrap
       ```

       [(출처: 커니의 안드로이드 이야기)](https://androidhuman.tistory.com/537)

     - 테스트하다가 build 실패하는 경우 src/test폴더를 지우고 다시 빌드해본다.

5. application.yml 파일을 작성한다.

6. build/libs 폴더로 들어가서 빌드된 파일을 실행한다.

   ```
   nohup java -jar {빌드된 파일} &
   (nohup 명령어를 사용하지 않으면 터미널을 종료했을 때 프로그램도 종료된다.)
   
   추가적인 설정도 가능하다.
   nohup java -jar -Dserver.port=8083 -Dspring.profiles.active=alpha {빌드된 파일} &
   ```

7. 실행완료.
   실행되고 있는지 확인하기 위해서 `ps -ef | grep jar` 명령어를 사용할 수 있다.

[출처: AWS EC2에 스프링 부트 프로젝트 배포하기](https://choihz.tistory.com/20)



백그라운드에 실행시켜놓은 파일 종료하기

1. PID를 찾는다

   ```
   ps -ef | grep java
   혹은
   ps -ef | grep jar
   ```

2. kill PID

   ```
   kill PID
   혹은
   kill -9 PID (강제종료한다)
   ```

   



# nginx

1. 설치

   ```
   sudo apt-get update (패키지 업데이트)
   sudo apt-get install nginx (nginx 설치)
   ( nginx -v 명령어를 통해 설치여부 및 버전을 확인할 수 있다. )
   ```

   

2. 실행

   ```
   sudo service nginx start (nginx 실행)
   혹은 sudo systemctl nginx start (nginx 실행)
   ( ps -ef | grep nginx 명령어를 통해 nginx가 잘 실행되었는지 확인할 수 있다. )
   ( 브라우저를 통해 EC2 Public DNS 주소로 들어가서 Welcome to nginx!가 보인다면 정상적으로 작동하는 것이다. )
   ```



- sites-available : sites-available 폴더: 가상 서버 환경에 대한 설정 파일들이 위치하는 디렉토리.
- sites-enabled : sites-available에 있는 가상서버 파일 중에 실행하고자 하는 파일을 symlink로 연결한 폴더. 이 폴더에 위치한 가상서버 환경 파일들을 읽어서 서버를 세팅한다.
- nginx.conf : nginx에 관한 설정파일로 내부에서 include 명령어를 사용하여 sites-enabled 폴더에 있는 파일들을 가져온다.

[출처: nginx 정리와 설치 및 기본 설정방법](https://wedul.site/579)



3. 기본 환경설정

   ```
   cd /etc/nginx/sites-available
   
   해당 경로에서 back.conf // front.conf을 각각 만들어 설정을 진행했다.
   ```

   front.conf (둘 다 합친거, 이름만 front임)

   ```nginx
   server {
   
           listen  80;
           listen [::]:80;
           server_name i3a108.p.ssafy.io;
   
   
           location / {
                   root /home/ubuntu/yj/s03p12a108/frontend/dist;
                   index index.html;
                   try_files $uri $uri/ /index.html;
           }
   
           location /api {
                   proxy_pass http://localhost:8080;
                   proxy_redirect off;
                   charset utf-8;
                   proxy_set_header X-Real_IP $remote_addr;
                   proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                   proxy_set_header X-Forwarded-Proto $scheme;
                   proxy_set_header X-NginX-Proxy true;
           }
   }
   ```

   

   DNS 설정 이후

   ```
   server {
   
           listen  80;
           listen [::]:80;
        server_name honeycombo.online;
   
   
           location / {
                   root /home/ubuntu/release/s03p13a108/frontend/dist;
                   index index.html;
                   try_files $uri $uri/ /index.html;
           }
   
           location /api {
                   proxy_pass http://localhost:8080;
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
           server_name www.honeycombo.online;
   
           location / {
                   return 301 http://honeycombo.online$request_uri;
           }
   }
   ```
   
   
   
   
   
   이후 sites-enabled 폴더로 이동하여 symlink로 sites-available의 원하는 파일을 연결한다.
   
   ```
   cd sites-enabled
   sudo ln -s ../sites-available/foo.conf .
   ls -l
   ```
   
   [출처: Stackoverflow](https://stackoverflow.com/questions/18089525/nginx-sites-enabled-sites-available-cannot-create-soft-link-between-config-fil)



설정이 끝나면 문법 체크하고 reload 해본다.

```
sudo nginx -t (문법 체크)
sudo nginx -s reload (reload configuration)
```



- nginx 명령어
  - `systemctl status nginx` : nginx가 active 상태인지 확인할 수 있다.