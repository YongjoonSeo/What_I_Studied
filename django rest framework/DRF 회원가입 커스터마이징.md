## DRF 회원가입 커스터마이징

### 1. 필요한 패키지 추가

- django-rest-auth
- django-allauth

<br>

<br>

### 2. django-allauth 커스터마이징

- **`serializers.py`와 `adapter.py`에서 기본적으로 패키지에서 제공하는 필드 외의 다른 필드를 저장하는 serializer와 adapter를 정의하여 사용한다.**

#### a. serializers.py

- `rest_auth.registration.serializers.RegisterSerializer`를 상속받아 회원가입 serializer를 커스터마이징 할 수 있다.
  - 이때 반드시 `save` 메소드를 정의해줘야 한다.

```python
# accounts/serializers.py

...
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

...
class CustomRegisterSerializer(serializers.ModelSerializer, RegisterSerializer):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2', 'latitude', 'longitude',
            'address', 'nickname', 'is_director', 'kindergarten_id'
        ]

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user
```

<br>

#### b. adapter.py

- `django-allauth/allauth/account/adapter.py`에 있는 `DefaultAccountAdapter`를 상속받아 회원가입을 커스터마이징 할 수 있다.
  - `adapter.py` 라는 파일을 만들어서 커스터마이징 한다.
- `settings.py`에서 커스터마이징 된 adapter를 사용하겠다고 등록한다.
- `allauth/account/utils.py`에 있는 `user_field`함수는 들어온 인자가 subscriptable 하지 않으면 에러가 난다.
  - user_field를 지정해주는 함수를 따로 만들어서 사용한다.

```python
# accounts/adapter.py

from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model


def custom_user_field(user, field, *args):
    """
    Sets (optional) user model fields. No-op if fields do not exist.
    """
    if not field:
        return
    User = get_user_model()
    try:
        field_meta = User._meta.get_field(field)
        max_length = field_meta.max_length
    except FieldDoesNotExist:
        if not hasattr(user, field):
            return
        max_length = None
    if args:
        # Setter
        v = args[0]
        if hasattr(v, "__getitem__"):
            v = v[0:max_length]
        setattr(user, field, v)
    else:
        # Getter
        return getattr(user, field)


class CustomUserAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """

        user = super().save_user(request, user, form, False)
        custom_user_field(user, 'latitude', request.data.get('latitude', None))
        custom_user_field(user, 'longitude', request.data.get('longitude', None))
        custom_user_field(user, 'address', request.data.get('address', None))
        custom_user_field(user, 'nickname', request.data.get('nickname', ''))
        custom_user_field(user, 'is_director', request.data.get('is_director', False))
        custom_user_field(user, 'kindergarten_id', request.data.get('kindergarten_id', 1))
        user.save()
        return user
```

- `hasattr` 함수를 이용하여 들어온 인자 v가 subscriptable 한지 판단하여, 만약 subscriptable한 인자라면 max_length 만큼만 저장한다.

<br>

### c. settings.py

- 커스터마이징한 serializer와 adapter를 settings에 등록한다.

```python
# settings/base.py

...
# rest auth registration template
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer'
}

# custom registration adapter
ACCOUNT_ADAPTER = 'accounts.adapter.CustomUserAccountAdapter'
```

<br>

<br>

<br>

<br>

참고자료

- [django-allauth github](https://github.com/pennersr/django-allauth/blob/master/allauth/account/adapter.py#L227)
- [django-rest-auth Documentation](https://django-rest-auth.readthedocs.io/en/latest/configuration.html)
- [stack overflow](https://stackoverflow.com/questions/37841612/django-rest-auth-custom-registration-fails-to-save-extra-fields)