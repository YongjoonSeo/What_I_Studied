## Django 회원가입 이메일 인증하기

### 1. Google 계정 관리

- Google 계정 -> 보안 -> 보안 수준이 낮은 앱의 액세스에서 보안 수준이 낮은 앱 허용을 `사용`으로 바꾼다.



### 2. settings.py에 email 등록

```python
# settings.py

...

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'http://childrenzip.site'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'http://childrenzip.site'

# email verification
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.googlemail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = secrets.get_secret('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = secrets.get_secret('EMAIL_HOST_PASSWORD')
```

```python
# urls.py
...
from allauth.account.views import confirm_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')), # rest_auth url 등록
    path('rest-auth/', include('accounts.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')), # 회원가입
    path('account/', include('allauth.urls')), # <<< 추가됨
    path('accounts-rest/registration/account-confirm-email/<str:key>/', confirm_email, name='account_confirm_email'), # <<< 추가됨
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # swagger
]
```





### 3. email 내용 커스터마이징

#### a. settings.py에 템플릿 경로 추가

```python
# settings/base.py

...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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
...
```



#### b. 템플릿 덮어쓰기

- `templates/account/email/email_confirmation_message.txt`
- `templates/account/email/email_confirmation_subject.txt`

#### c. 사이트 도메인 만들어서 지정하기

1. `python manage.py createsuperuser` 명령어를 통해 관리자 계정을 만든다.
2. django admin페이지에서 site를 만든다.
3. `django_site` 테이블에서 만든 site의 id를 보고, `settings.py`의 `SITE_ID` 변수를 해당 id로 지정한다.



참고자료

- [django-allauth Documentation](https://django-allauth.readthedocs.io/en/latest/configuration.html)
- [django-allauth Github](https://github.com/pennersr/django-allauth/tree/master/allauth/templates/account/email)
- [코드포휴먼](https://code4human.tistory.com/entry/Django-REST-FrameworkDRF-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0?category=785473)
- [DEV-YAKUZA](https://dev-yakuza.github.io/ko/django/gmail-smtp/)
- [KRAKEN](https://krakensystems.co/blog/2020/custom-users-using-django-rest-framework)

