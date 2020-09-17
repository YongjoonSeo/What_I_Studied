## DataFrame 인덱싱 & 슬라이싱

- Pandas에서 row는 **index**라고 부른다.
- 기본적으로 df.loc['index', 'column']의 경우 **행**, df['column']의 경우 **열**을 가리킬 때 쓴다고 생각하면 편하다.

### 1. df.loc['index', 'column']

- 행 또는 열을 가리키거나 슬라이싱할 때 쓸 수 있다.

<br>

<br>

### 2. df['column']

- 열을 가리키거나 행을 슬라이싱할 때 쓸 수 있다.
  - 기본적으로 열을 가리킬 때 쓰지만, 예외적으로 슬라이싱하면 **행을 슬라이싱한다는 특징**을 잘 알아둬야 한다.

<br>

<br>

### 3. df.iloc['index', 'column']

<br>

<br>

### 4. Boolean Indexing

<br>

<br>

<br>

<br>

- 참고문서
  - [Pandas Documentation](https://pandas.pydata.org/docs/index.html)