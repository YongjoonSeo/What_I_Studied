## NumPy

### 1. NumPy Array를 만드는 방법

#### a. 리스트를 직접 넣어 만들기

##### i. numpy.array

- numpy.array(*object*, *dtype=None*, ***, *copy=True*, *order='K'*, *subok=False*, *ndmin=0*) [reference](https://numpy.org/doc/stable/reference/generated/numpy.array.html?highlight=numpy array#numpy.array)

  ```python
  import numpy as np
  
  arr1 = np.array([1, 3, 5, 7, 9, 2, 4, 6, 8])
  arr2 = np.array([[1, 3, 5, 7], [2, 4, 6, 8], [9, 11, 10, 12]])
  ```

- numpy를 import할 때 일반적으로 np로 줄여서 사용한다.

- 콘솔에 `arr1`이라고 입력하면 `array([1, 3, 5, 7, 9, 2, 4, 6, 8])`이 출력된다.

- 콘솔에 `arr2`라고 입력하면 다음과 같이 출력된다.

  ```
  array([[ 1,  3,  5,  7],
         [ 2,  4,  6,  8],
         [ 9, 11, 10, 12]])
  ```

- `type(arr1)` 명령어로 `arr1`의 타입을 알아보면 `numpy.ndarray`가 출력된다.

  - `ndarray`는 n-dimensional array의 줄임말로 n차원 배열이라는 뜻이다.
  - `arr2`도 같은 타입이다.

<br>

#### b. 모든 요소의 값을 동일하게 만들기

##### i. numpy.full

- numpy.full(*shape*, *fill_value*, *dtype=None*, *order='C'*) [reference](https://numpy.org/doc/stable/reference/generated/numpy.full.html?highlight=full#numpy.full) [source](https://github.com/numpy/numpy/blob/v1.19.0/numpy/core/numeric.py#L268-L316)

- 원하는 모양 대로 배열을 만드는데, 이때 원하는 값으로만 채운다.

  ```python
  arr3_1 = np.full(5, 8)
  arr3_2 = np.full(5, 0)
  arr3_3 = np.full(5, 1)
  arr3_4 = np.full((3,4), 1)
  
  arr3_1
  # 출력: array([8, 8, 8, 8, 8])
  arr3_2
  # 출력: array([0, 0, 0, 0, 0])
  arr3_3
  # 출력: array([1, 1, 1, 1, 1])
  arr3_4
  # 출력: array([[1, 1, 1, 1],
  #		      [1, 1, 1, 1],
  #		      [1, 1, 1, 1]])
  ```

- 모든 출력은 한 줄 한 줄 콘솔에 입력하여 얻는다.

<br>

##### ii. numpy.zeros

- numpy.zeros(*shape*, *dtype=float*, *order='C'*) [reference](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html?highlight=zeros#numpy.zeros)

- 원하는 모양 대로 배열을 만드는데, 이때 0으로만 채운다.

  ```python
  arr4 = np.zeros(5, dtype=int)
  arr4
  # 출력: array([0, 0, 0, 0, 0])
  ```

- `arr3_2` 와 같은 행렬이 반환된다.
- dtype (데이터타입) 인자의 디폴트 값은 float이기 때문에 `dtype=int` 를 통해 데이터를 정수형으로 바꿔주었다.

<br>

##### iii. numpy.ones

- numpy.ones(*shape*, *dtype=None*, *order='C'*) [reference](https://numpy.org/doc/stable/reference/generated/numpy.ones.html?highlight=ones#numpy.ones) [source](https://github.com/numpy/numpy/blob/v1.19.0/numpy/core/numeric.py#L144-L194)

- 원하는 모양 대로 배열을 만드는데, 이때 1로만 채운다.

  ```python
  arr5 = np.ones(5, dtype=int)
  arr5
  # 출력: array([1, 1, 1, 1, 1])
  ```

- `arr3_3` 과 같은 행렬이 반환된다.
- dtype (데이터타입) 인자의 디폴트 값은 float이기 때문에 `dtype=int` 를 통해 데이터를 정수형으로 바꿔주었다.

<br>

#### c. 무작위 값으로 만들기

##### i. numpy.random.random

- numpy.random.random(*size=None*) [reference](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html?highlight=random#numpy.random.random)

- 무작위 값이 들어간 배열을 원하는 모양 대로 만든다.

  ```python
  arr6_1 = np.random.random(5)
  arr6_2 = np.random.random((3, 4))
  
  arr6_1
  # 출력: array([0.01033496, 0.18648639, 0.15662307, 0.43724582, 0.71128176])
  # 이 출력은 매번 달라진다.
  arr6_2
  # 출력: array([[0.20503991, 0.34227621, 0.07132553, 0.8415706 ],
  #		      [0.26564224, 0.95131766, 0.22962277, 0.00985909],
  #    		  [0.53824821, 0.89246074, 0.46764977, 0.96426091]])
  # 이 출력은 매번 달라진다.
  ```

<br>

#### d. 연속적인 값으로 만들기

##### i. numpy.arange

- numpy.arange([*start*, ]*stop*, [*step*, ]*dtype=None*) [reference](https://numpy.org/doc/stable/reference/generated/numpy.arange.html?highlight=arange#numpy.arange)

- 한정된 구간 내에서 일정한 간격으로 값을 넣어 배열을 만든다.

  ```python
  arr7_1 = np.arange(8)
  arr7_2 = np.arange(3, 8)
  arr7_3 = np.arange(3, 8, 2)
  
  arr7_1
  # 출력: array([0, 1, 2, 3, 4, 5, 6, 7])
  # 0부터 8까지 1의 간격으로 값을 넣어 배열을 만든다. (8은 미포함)
  arr7_2
  # 출력: array([3, 4, 5, 6, 7])
  # 3부터 8까지 1의 간격으로 값을 넣어 배열을 만든다. (8은 미포함)
  arr7_3
  # 출력: array([3, 5, 7])
  # 3부터 8까지 2의 간격으로 값을 넣어 배열을 만든다. (8은 미포함)
  ```

<br>

<br>

### 2. NumPy Array 속성 알아보기

```python
arr1 = np.array([1, 3, 5, 7, 9, 2, 4, 6, 8])
arr2 = np.array([[1, 3, 5, 7], [2, 4, 6, 8], [9, 11, 10, 12]])
arr1.shape
# 출력: (9,)
arr2.shape
# 출력: (3, 4)
arr1.size
# 출력: 9
arr2.size
# 출력: 12
```

- 모든 출력은 한 줄 한 줄 콘솔에 입력하여 얻는다.

<br>

#### a. ndarray.shape

- 배열의 모양을 나타내는 튜플이다.
- `arr1`은 1차원 배열에 항목이 9개 있으므로 `(9,)`와 같이 나타난다. (파이썬 문법상 튜플의 요소가 하나면 뒤에 콤마(`,`)가 온다)
- `arr2`는 2차원 배열에 3개의 행, 4개의 열이 있으므로 `(3, 4)`와 같이 나타난다.

<br>

#### b. ndarray.size

- 배열의 요소 수를 나타낸다.
- `arr1` 의 요소 개수는 9개, `arr2`의 요소 개수는 12개이므로 각각 9와 12라는 값을 보여준다.

<br>

<br>

### 3. 인덱싱, 슬라이싱

#### a. 인덱싱

- 기존 파이썬에서의 인덱싱과 같은 방법으로도 NumPy 배열을 인덱싱 할 수 있다.

  ```python
  arr1 = np.array([1, 3, 5, 7, 9, 2, 4, 6, 8])
  print(arr1[0])
  print(arr1[3])
  print(arr1[-1])
  
  # 출력
  1
  7
  8
  ```

- 리스트를 활용하여 인덱싱 할 수 있다.

  ``` python
  arr1[[1, 3, 4]]
  
  # 출력: array([3, 7, 9])
  ```

  ```python
  arr1_2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
  arr1_2[[0, 1], [1,2]]
  
  # 출력: array([2, 7])
  ```

- NumPy 배열로도 인덱싱 할 수 있다.

  ```python
  arr2 = np.array([2, 4, 8])
  arr1[arr2]
  
  # 출력: array([5, 9, 8])
  ```

<br>

#### b. 슬라이싱

- 기존 파이썬에서의 슬라이싱과 같은 방법으로 NumPy 배열을 슬라이싱 할 수 있다.

  ```python
  arr1 = numpy.array([1, 3, 5, 7, 9, 2, 4, 6, 8])
  
  arr1[:3]
  # 출력: array([1, 3, 5])
  arr1[2:5]
  # 출력: array([5, 7, 9])
  arr1[3:8:2]
  # 출력: array([7, 2, 6])
  ```

<br>

<br>

### 4. NumPy Array 연산 및 메소드

#### a. 사칙연산

```python
arr1 = np.arange(5)
arr2 = arr1 * 2
arr3 = arr1 / 2
arr4 = arr1 ** 2

arr1
# 출력: array([0, 1, 2, 3, 4])
arr2
# 출력: array([0, 2, 4, 6, 8])
arr3
# 출력: array([0. , 0.5, 1. , 1.5, 2. ])
arr4
# 출력: array([ 0,  1,  4,  9, 16], dtype=int32)
```

```python
arr1 = np.arange(5)
arr2 = np.arange(5, 10)

arr1
# 출력: array([0, 1, 2, 3, 4])
arr2
# 출력: array([5, 6, 7, 8, 9])
arr1 + arr2
# 출력: array([ 5,  7,  9, 11, 13])
arr1 * arr2
# 출력: array([ 0,  6, 14, 24, 36])
arr1 / arr2
# 출력: array([0.        , 0.16666667, 0.28571429, 0.375     , 0.44444444])
```

<br>

#### b. Boolean 연산

##### i. 기본적인 Boolean 연산

```python
arr1 = numpy.array([1, 3, 5, 7, 9, 2, 4, 6, 8])

arr1 > 5
# 출력: array([False, False, False,  True,  True, False, False,  True,  True])
arr1 % 2 == 1
# 출력: array([ True,  True,  True,  True,  True, False, False, False, False])
# 홀수 값만 True로 표현된다.
```

<br>

##### ii. numpy.where

- numpy.where(*condition*[, *x*, *y*]) [reference](https://numpy.org/doc/stable/reference/generated/numpy.where.html?highlight=where#numpy.where)

- 조건이 참인 요소의 인덱스를 ndarray로 묶어 반환한다.

  ```python
  a = np.arange(10, 20)
  
  a
  # 출력: array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
  np.where(b < 15)
  # 출력: (array([0, 1, 2, 3, 4], dtype=int64),)
  ```

  ```python
  b = np.arange(5, 10)
  c = np.where(b % 2 == 0)
  
  b
  # 출력: array([5, 6, 7, 8, 9])
  b[c]
  # 출력: array([6, 8])
  ```

<br>

#### c. NumPy 통계 메소드

##### i. numpy.ndarray.max

- ndarray.max(*axis=None*, *out=None*, *keepdims=False*, *initial=<no value>*, *where=True*) [reference](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html?highlight=max#numpy.ndarray.max)

- NumPy 배열에서 가장 큰 값을 반환한다.

  ```python
  arr1 = np.array([1, 7, 8, 5, 9, 2, 3, 4])
  arr2 = np.array([[0, 4, 2, 7], [3, 5, 8, 6]])
  
  print(arr1.max())
  print(arr2.max())
  
  # 출력
  9
  8
  ```

<br>

##### ii. numpy.ndarray.min

- ndarray.min(*axis=None*, *out=None*, *keepdims=False*, *initial=<no value>*, *where=True*) [reference](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.min.html?highlight=min#numpy.ndarray.min)

- NumPy 배열에서 가장 작은 값을 반환한다.

  ```python
  arr1 = np.array([1, 7, 8, 5, 9, 2, 3, 4])
  arr2 = np.array([[0, 4, 2, 7], [3, 5, 8, 6]])
  
  print(arr1.min())
  print(arr2.min())
  
  # 출력
  1
  0
  ```

<br>

##### iii. numpy.ndarray.mean

- ndarray.mean(*axis=None*, *dtype=None*, *out=None*, *keepdims=False*) [reference](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.mean.html?highlight=mean#numpy.ndarray.mean)

- NumPy 배열에 있는 모든 요소들의 평균값을 반환한다.

  ```python
  arr1 = np.array([1, 7, 8, 5, 9, 2, 3, 4])
  arr2 = np.array([[0, 4, 2, 7], [3, 5, 8, 6]])
  
  print(arr1.mean())
  print(arr2.mean())
  
  # 출력
  4.875
  4.375
  ```

<br>

##### iv. numpy.median

- numpy.median(*a*, *axis=None*, *out=None*, *overwrite_input=False*, *keepdims=False*) [reference](https://numpy.org/doc/stable/reference/generated/numpy.median.html?highlight=median#numpy.median) [source](https://github.com/numpy/numpy/blob/v1.19.0/numpy/lib/function_base.py#L3438-L3525)

- NumPy 배열에서 중앙값을 반환한다.

  ```python
  arr1 = np.array([1, 7, 8, 5, 9, 2, 3, 4])
  arr2 = np.array([[0, 4, 2, 7], [3, 5, 8, 6]])
  
  print(np.median(arr1))
  print(np.median(arr2))
  
  # 출력
  4.5
  4.5
  ```

<br>

##### v. numpy.ndarray.var

- ndarray.var(*axis=None*, *dtype=None*, *out=None*, *ddof=0*, *keepdims=False*) [reference](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.var.html?highlight=var#numpy.ndarray.var)

- NumPy 배열의 분산을 반환한다.

  ```python
  arr1 = np.array([1, 7, 8, 5, 9, 2, 3, 4])
  arr2 = np.array([[0, 4, 2, 7], [3, 5, 8, 6]])
  
  print(arr1.var())
  print(arr2.var())
  
  # 출력
  7.359375
  6.234375
  ```

<br>

##### v. numpy.ndarray.std

- ndarray.std(*axis=None*, *dtype=None*, *out=None*, *ddof=0*, *keepdims=False*) [reference](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.std.html?highlight=std#numpy.ndarray.std)

- NumPy 배열의 표준편차를 반환한다.

  ```python
  arr1 = np.array([1, 7, 8, 5, 9, 2, 3, 4])
  arr2 = np.array([[0, 4, 2, 7], [3, 5, 8, 6]])
  
  print(arr1.std())
  print(arr2.std())
  
  # 출력
  2.7128168017763383
  2.496873044429772
  ```

<br>

<br>

<br>

<br>

[출처: NumPy.org](https://numpy.org/doc/stable/index.html)