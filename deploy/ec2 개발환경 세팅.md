## ec2 개발환경 세팅

설치에 필요한 라이브러리 다운로드.

- sudo apt-get update
- sudo apt-get install -y vim git wget
- sudo apt-get install build-essential checkinstall
- sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
  libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev



파이썬 다운로드.

- mkdir setupfile
- cd setupfile
- sudo wget https://www.python.org/ftp/python/3.7.6/Python-3.7.6.tgz
- sudo tar xzf Python-3.7.6.tgz



파이썬 컴파일.

- cd Python-3.7.6
- sudo ./configure --enable-optimizations
- sudo make altinstall



설치한 파이썬 파일을 python 커맨드의 디폴트로 설정하기

- sudo update-alternatives --install /usr/bin/python python /usr/local/bin/python3.8 1



확인

- python -V



pip 설치

- sudo apt install python-pip
- pip3을 pip 디폴트로 설정하기
  
  - sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
  
  - 안되면 밑의 방법으로 하기.
  
    ```
    sudo rm /usr/bin/pip
    sudo ln -s /usr/bin/pip3.6 /usr/bin/pip
    ```



**mysqlclient 설치에서 오류 나면 `sudo apt-get install libmysqlclient-dev` 명령어로 이 패키지를 한번 깔아본다.**

---

MySQL

- sudo apt update (패키지 업데이트)
- sudo apt install mysql-server (MySQL 서버 설치)
- sudo mysql -u root -p (MySQL 접속)



ubuntu root mysql password 재설정
https://freestrokes.tistory.com/43

---

gunicorn

- pip install gunicorn
- gunicorn --bind 0.0.0.0:8000 {프로젝트 이름}.wsgi:application 으로 확인
  - 단순하게 생각하면 `python manage.py runserver`를 했을 때 처럼 작동한다.

---

nginx

- sudo apt-get update (패키지 업데이트)

- sudo apt-get install nginx (nginx 설치)

  ( nginx -v 명령어를 통해 설치여부 및 버전을 확인할 수 있다. )

---

yarn

- ModuleNotFoundError: No module named 'cliapp'이 뜨는 경우



- 참고자료
  - [We On Fire님 블로그](https://dlehdgml0480.tistory.com/8)