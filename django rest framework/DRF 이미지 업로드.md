## DRF 이미지 업로드

### 1. 패키지 설치 및 설정

- pillow 설치

- media 폴더 추가

- settings.py 에 media 경로 추가

  ```python
  # settings/base.py
  
  ...
  # for image upload
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  ```

- urls.py에 static 경로 추가

  ```python
  # urls.py
  ...
  from django.conf import settings
  from django.conf.urls.static import static
  
  ...
  urlpatterns = [
      ...
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

  

### 2. models.py

- 원하는 모델에 **ImageField**를 이용하여 이미지를 업로드할 수 있다.

  - `upload_to`옵션을 통해 파일을 저장할 폴더를 지정할 수 있다.

  ```python
  # accounts/models.py
  
  class User(AbstractUser):
      nickname = models.CharField(max_length=50)
      profile_image = models.ImageField(upload_to="profile/%Y/%m/%d", null=True)
  ```



### 3. adapter.py

- 회원가입을 커스터마이징 한 경우 `adapter.py`에서도 파일이 저장될 수 있도록 해야한다.

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
          custom_user_field(user, 'profile_image', request.data.get('profile_image', None))
          user.save()
          return user
  ```

  





참고자료

- [프리킴의 개발로그](https://freekim.tistory.com/9)
- [Django Documentation](https://docs.djangoproject.com/en/3.1/)