## drf-yasg 커스터마이징

![after_docstring](https://i.ibb.co/8B53wfM/swagger-docstring2.jpg)

- 이 상태에서는 어떤 데이터를 요청으로 넘겨줘야할지도 모르고, 어떤 응답을 받는지도 모른다.
  
  - 필요한 정보를 기입하기 위해 커스터마이징이 필요하다.
  - 현재 `article_create`의 모습
  
  ```python
  # community/views.py
  
  @api_view(['POST'])
  @permission_classes([IsAuthenticated])
  def article_create(request):
      """
      게시글 생성
  
      ## 게시글 생성
      - 로그인한 사용자만 요청할 수 있다.
      """
      serializer = ArticleSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(user=request.user)
      return Response(serializer.data)
  ```

<br>

<br>

### 1. Request 커스터마이징

#### a. header 넣기

- 인증된 사용자만 `article_create`함수를 호출할 수 있도록 했다. 토큰을 사용하여 인증관리를 하고 있으므로, `header`에 토큰 정보를 함께 넘겨줘야 한다.

- `request_schemas.py`라는 파일을 만들어서 API 문서의 요청 부분을 커스텀할 때 쓸 것이다.

  ```python
  # community/request_schemas.py
  
  from drf_yasg import openapi
  
  header = openapi.Parameter(
      'Authorization',
      openapi.IN_HEADER,
      description='"Token {키값}"의 형태로 토큰을 입력하세요.',
      type=openapi.TYPE_STRING
  )
  ```

  ```python
  # community/views.py
  
  ...
  from drf_yasg.utils import swagger_auto_schema
  from . import request_schemas
  
  @swagger_auto_schema(
      method='post',
      manual_parameters=[request_schemas.header]
  )
  @api_view(['POST'])
  @permission_classes([IsAuthenticated])
  def article_create(request):
      """
      게시글 생성
  
      ## 게시글 생성
      - 로그인한 사용자만 요청할 수 있다.
      """
      serializer = ArticleSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(user=request.user)
      return Response(serializer.data)
  
  ...
  ```

- `views.py`에서 `@swagger_auto_schema` 어노테이션을 통해 API 문서를 커스텀할 수 있다. `manual_parameters` 인자를 사용하여 입력값으로 지정할 파라미터를 리스트 형식으로 넣는다.

- `openapi.Parameter`를 통해 header를 입력 인자로 지정하고 원하는 설명을 쓴다. [(참고: openapi.Parameter)](https://drf-yasg.readthedocs.io/en/stable/drf_yasg.html#drf_yasg.openapi.Parameter)

  - `openapi.IN_HEADER`부분이 이 파라미터가 header라는 것을 명시하는 역할을 한다.

- 다음과 같은 결과가 나온다.

![custom1](https://i.ibb.co/6g8Htnd/custom-swagger1.jpg)

<br>

#### b. query 넣기

- 마찬가지로 `request_schemas.py`에서 입력받을 `title`과 `content`를 Parameter로 설정해보자.

  ```python
  # community/request_schemas.py
  
  from drf_yasg import openapi
  
  header = openapi.Parameter(
      'Authorization',
      openapi.IN_HEADER,
      description='"Token {키값}"의 형태로 토큰을 입력하세요.',
      type=openapi.TYPE_STRING
  )
  
  title = openapi.Parameter(
      'title',
      openapi.IN_QUERY,
      description='글 제목',
      type=openapi.TYPE_STRING
  )
  
  content = openapi.Parameter(
      'content',
      openapi.IN_QUERY,
      description='글 내용',
      type=openapi.TYPE_STRING
  )
  ```

  ```python
  # community/views.py
  
  ...
  @swagger_auto_schema(
      method='post',
      manual_parameters=[
          request_schemas.header,
          request_schemas.title,
          request_schemas.content
      ]
  )
  @api_view(['POST'])
  @permission_classes([IsAuthenticated])
  def article_create(request):
      """
      게시글 생성
  
      ## 게시글 생성
      - 로그인한 사용자만 요청할 수 있다.
      """
      serializer = ArticleSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(user=request.user)
      return Response(serializer.data)
  ...
  ```

- `title`과 `content`를 설정하는 방법도 `header`를 설정하는 방법과 유사하다. 

  - 이때 `openapi.IN_HEADER` 대신 `openapi.IN_QUERY`를 사용하여 query로써 요청이 전달되도록 설정했다.

- 다음과 같은 결과가 나온다.

![custom2](https://i.ibb.co/px2zRdQ/custom-swagger2.jpg)

- 하지만 이와 같은 방법으로는 글을 쓸 수 없다. `title`과 `content`가 `body`가 아닌 `query`에 담겨 요청이 보내지기 때문이다.

<details><summary>Swagger로 요청 보낸 결과</summary><img src="https://i.ibb.co/HqwYszX/custom-swagger2-res.jpg"></details>

<br>

#### c. body 넣기

- 원하는 데이터를 body에 넣어 요청하기 위해서는 `swagger_auto_schema`의 `request_body`인자를 설정해줘야 한다.

  - 이때 `request_body` 인자로는 `openapi.Schema` 또는 `serializer`와 같은 것이 들어가야 한다.

- 따라서 request 형태에 맞는 `serializer`를 별도로 구성하여 `request_body`를 설정할 것이다.

  ```python
  # community/request_schemas.py
  
  from drf_yasg import openapi
  from rest_framework import serializers
  from .models import Article
  
  header = openapi.Parameter(
      'Authorization',
      openapi.IN_HEADER,
      description='"Token {키값}"의 형태로 토큰을 입력하세요.',
      type=openapi.TYPE_STRING
  )
  
  class ArticleCreateRequest(serializers.ModelSerializer):
      class Meta:
          model = Article
          fields = ['title', 'content']
  ```

  ```python
  # community/views.py
  
  ...
  @swagger_auto_schema(
      method='post',
      request_body=request_schemas.ArticleCreateRequest,
      manual_parameters=[request_schemas.header]
  )
  @api_view(['POST'])
  @permission_classes([IsAuthenticated])
  def article_create(request):
      """
      게시글 생성
  
      ## 게시글 생성
      - 로그인한 사용자만 요청할 수 있다.
      """
      serializer = ArticleSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(user=request.user)
      return Response(serializer.data)
  ...
  ```

- `request_schemas.py`에서 `title`과 `content`만 필드로 가지는 `serializer`를 설정해주었다.

  - 이렇게 만든 `serializer`로 `request_body`를 설정하면 다음과 같은 결과를 얻을 수 있다.

![custom3](https://i.ibb.co/Sf67mRj/custom-swagger3.jpg)

<details><summary>Swagger로 요청 보낸 결과 - 잘 된다!</summary><img src="https://i.ibb.co/wdmrptB/custom-swagger3-res.jpg"></details>

<br>

<br>

### 2. Response 커스터마이징

#### a. 기본적인 방법

- `swagger_auto_schema`의 `responses`인자에 딕셔너리 형태로 내용을 넣으면 된다.

  - 키는 상태코드, 값은 해당 상태코드일 때 보여줄 메시지를 입력한다.

  ```python
  # community/views.py
  
  ...
  @swagger_auto_schema(
      method='post',
      request_body=request_schemas.ArticleCreateRequest,
      manual_parameters=[request_schemas.header],
      responses={
          201: ArticleSerializer
      }
  )
  @api_view(['POST'])
  @permission_classes([IsAuthenticated])
  def article_create(request):
      """
      게시글 생성
  
      ## 게시글 생성
      - 로그인한 사용자만 요청할 수 있다.
      """
      serializer = ArticleSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(user=request.user)
      return Response(serializer.data, status=201)
  ...
  ```

- HTTP 상태 코드가 201인 경우 `ArticleSerializer`의 형태 대로 응답한다는 내용을 API 문서에 기록할 수 있다.

- 글이 성공적으로 생성될 때의 HTTP 상태 코드는 201 Created이 적절하므로 `Response(serializer.data, status=201)`부분을 통해 알맞은 상태 코드가 반환되도록 설정하였다.

- 다음과 같은 결과가 나온다.

![custom4](https://i.ibb.co/Ksn6d1c/custom-swagger4.jpg)

<details><summary>Swagger로 요청 보낸 결과</summary><img src="https://i.ibb.co/zbKrHRL/custom-swagger4-res.jpg"></details>

- 문서에는 `"comments": "string"`이라고 표기되어 있지만 실제로는 `"comments": []`와 같은 형태로 응답이 오고있다.

<br>

#### b. SerializerMethodField를 쓰는 경우

- `SerializerMethodField`를 사용하여 필드를 설정한 경우, 이 필드를 사용하기 위해 정의한 메소드에 swagger 관련 설정을 해줘야 한다.

  ```python
  # community/serializers.py
  
  ...
  from drf_yasg.utils import swagger_serializer_method
  
  
  class CommentForArticleSerializer(serializers.ModelSerializer):
      user = ArticleUserSerializer
      class Meta:
          model = Comment
          fields = ['content', 'created_at', 'user']
  
  class ArticleSerializer(serializers.ModelSerializer):
      user = ArticleUserSerializer(required=False)
      # comments = serializers.SlugRelatedField(many=True, read_only=True, slug_field='content')
      # comments = CommentListingField(many=True, read_only=True)   
      comments = serializers.SerializerMethodField()
  
      class Meta:
          model = Article
          fields = '__all__'
  
      @swagger_serializer_method(serializer_or_field=CommentForArticleSerializer)
      def get_comments(self, article):
          comments = Comment.objects.filter(article=article).order_by('-created_at')
          serializer = CommentForArticleSerializer(instance=comments, many=True)
          return serializer.data
  ...
  ```

- 다른 추가적인 설정 없이 다음과 같은 결과를 얻을 수 있다.

![custom5](https://i.ibb.co/QjC63Gp/custom-swagger5.jpg)

<br>

<br>

<br>

<br>

- 참고자료
  - [drf-yasg Documentation](https://drf-yasg.readthedocs.io/en/stable/index.html)
  - [rubycho님의 블로그](https://velog.io/@rubycho/%EB%AC%B8%EC%84%9C%ED%99%94%EB%A5%BC-%EC%9C%84%ED%95%9C-drf-yasg-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0#custom-response)
  - [타운컴퍼니 기술블로그](https://medium.com/towncompany-engineering/%EC%B9%9C%EC%A0%88%ED%95%98%EA%B2%8C-django-rest-framework-api-%EB%AC%B8%EC%84%9C-%EC%9E%90%EB%8F%99%ED%99%94%ED%95%98%EA%B8%B0-drf-yasg-c835269714fc)
  - [Django rest framework Documentations](https://www.django-rest-framework.org/)

