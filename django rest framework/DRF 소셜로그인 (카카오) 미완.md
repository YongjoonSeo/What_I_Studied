## DRF 소셜로그인 (카카오)

### 1. 소셜로그인 흐름 및 준비

![kakao sociallogin](https://developers.kakao.com/docs/latest/ko/assets/style/images/kakaologin/kakaologin_process.png)

#### a. 내 애플리케이션 만들기

#### b. 웹 등록하기

#### c. 카카오 로그인 활성화

- Redirect URI도 설정하기 (allauth 설정에 따라서.)
- 카카오 로그인 동의항목 설정



### 2. 필요한 패키지 설치

#### a. 패키지 설치

- django-rest-auth
- django-allauth

#### b. settings.py에 등록



### 3. 로직 작성

- **반드시 https로 요청을 보내야한다.**

#### a. 인증 코드 요청

#### b. 인증 코드로 토큰 요청

#### c. 토큰으로 API 호출



참고자료

- [코드포휴먼](https://code4human.tistory.com/entry/Django-Django-REST-frameworkDRF-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C-%EC%86%8C%EC%85%9C%EB%A1%9C%EA%B7%B8%EC%9D%B8kakao-%EA%B5%AC%ED%98%84-%EA%B8%B0%EB%A1%9D?category=785473)
- [django-allauth Github](https://github.com/pennersr/django-allauth)
- [django-rest-auth Documentation](https://django-rest-auth.readthedocs.io/en/latest/index.html)
- [**michaël's blog**](https://michaeldel.github.io/)
- [kakao developers](https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api)
- [개발의민족](https://velog.io/@snoop2head/2020-django-social-login-naver-google-kakao#kakaotalk)