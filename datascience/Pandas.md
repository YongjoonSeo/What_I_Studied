## Pandas

### 1. Pandas 개요

- Pandas란?
  - 관계형 데이터를 다루기 위한 파이썬 패키지
  - NumPy를 기반으로 만들어짐
- Pandas의 자료구조
  - Series
    - *class* pandas.Series(*data=None*, *index=None*, *dtype=None*, *name=None*, *copy=False*, *fastpath=False*) [reference](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series) [source](https://github.com/pandas-dev/pandas/blob/v1.1.1/pandas/core/series.py#L139-L4979) 
    - 축 라벨을 포함한 1차원 ndarray
    - 축 라벨은 **index**라고 불린다.
    - 어떤 자료형이든 담을 수 있다.
  - DataFrame
    - *class* pandas.DataFrame(*data=None*, *index=None*, *columns=None*, *dtype=None*, *copy=False*) [reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html?highlight=dataframe#pandas.DataFrame) [source](https://github.com/pandas-dev/pandas/blob/v1.1.1/pandas/core/frame.py#L340-L9261)
    - 여러 자료형을 담을 수 있는 2차원의 표 데이터
    - Series를 담고있는 컨테이너로도 볼 수 있다.
    - 행 라벨은 **index**, 열 라벨은 **columns**라고 불린다.

<br>

<br>

### 2. Pandas의 자료구조 다루기

#### a. Series 만들기

##### i. ndarray로

```python
import numpy as np
import pandas as pd

s = pd.Series(np.random.randn(5))
s
# 출력
0   -1.358608
1    1.143060
2   -0.266342
3    0.409451
4    0.689405
dtype: float64
    
s.index
# 출력: RangeIndex(start=0, stop=5, step=1)
```

```python
s_2 = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
s_2
# 출력
a    0.640898
b    0.311585
c   -0.849497
d   -0.878118
e   -1.093313
dtype: float64
    
s_2.index
# 출력: Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
```

- numpy.random.randn은 표준 정규 분포를 이루게끔 무작위 값을 추출하는 함수이다.
  - numpy.random.randn(*d0*, *d1*, *...*, *dn*) [reference](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html?highlight=randn#numpy.random.randn)
- ndarray를 사용하는 경우 **index**는 데이터의 길이와 같아야 한다.
- dtype은 데이터타입을 의미한다.

<br>

##### ii. 파이썬 딕셔너리로

```python
d = {'b': 1, 'a': 0, 'c': 2}
pd.Series(d)
# 출력
b    1
a    0
c    2
dtype: int64
```

```python
pd.Series(d, index=['b', 'c', 'd', 'a'])
# 출력
b    1.0
c    2.0
d    NaN
a    0.0
dtype: float64
```

- Pandas에서 빈 값을 표시할 때는 `NaN`이라고 나타난다.

<br>

##### iii. 스칼라 값으로

```python
pd.Series(5, index=['a', 'b', 'c', 'd', 'e'])
# 출력
a    5
b    5
c    5
d    5
e    5
dtype: int64
```

- **index**길이 만큼 주어진 값이 반복되는 방식으로 Series가 만들어진다.
- 스칼라 값을 사용할 땐 index가 반드시 주어져야 한다.

<br>

#### b. DataFrame 만들기

##### i. 딕셔너리로

###### (1) dict of Series

```python
dictionary = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
}

df = pd.DataFrame(dictionary)
df
# 출력
 	one 	two
a 	1.0 	1
b 	2.0 	2
c 	3.0 	3
d 	NaN 	4

pd.DataFrame(dictionary, index=['d', 'b', 'a'])
# 출력
 	one 	two
d 	NaN 	4
b 	2.0 	2
a 	1.0 	1

pd.DataFrame(dictionary, index=['d', 'b', 'a'], columns=['two', 'three'])
# 출력
 	two 	three
d 	4 		NaN
b 	2 		NaN
a 	1 		NaN
```

- Series의 원하는 index만으로 이루어진 DataFrame을 만들 수 있다.
- columns 인자를 통해 column에 라벨을 달 수 있다.
- 마지막 DataFrame에서는 `'three'` column의 데이터가 없기 때문에 `NaN`으로 표시되는 것을 볼 수 있다.

<br>

###### (2) dict of lists

```python
d = {
    'one': [1, 2, 3, 4], 
    'two': [4, 3, 2, 1]
}
pd.DataFrame(d, index=['a', 'b', 'c', 'd'])
# 출력
 	one two
a 	1 	4
b 	2 	3
c 	3 	2
d 	4 	1
```

- 딕셔너리의 key값이 column의 라벨이 되는 것을 볼 수 있다.

<br>

###### (3) dict of ndarrays

```python
d = {
    'one': np.array([1, 2, 3, 4]), 
    'two': np.array([4, 3, 2, 1])
}
pd.DataFrame(d, index=['a', 'b', 'c', 'd'])
# 출력
 	one two
a 	1 	4
b 	2 	3
c 	3 	2
d 	4 	1
```

<br>

##### ii. 리스트로

###### (1) list of dicts

```python
data = [
    {'a': 1, 'b': 2},
    {'a': 5, 'b': 10, 'c': 20}
]
pd.DataFrame(data, index=['first', 'second'])
# 출력
 		a 	b 	c
first 	1 	2 	NaN
second 	5 	10 	20.0
```

- 각 딕셔너리의 key값이 DataFrame의 column이 되는 것을 볼 수 있다.

<br>

###### (2) list of lists

```python
data = [
    ['tom', 10], 
    ['nick', 15], 
    ['juli', 14]
]
pd.DataFrame(data)
# 출력
 	0 		1
0 	tom 	10
1 	nick 	15
2 	juli 	14
```

- list의 모든 요소는 DataFrame의 데이터 값이 된다.

<br>

###### (3) list of Series

```python
data = [
    pd.Series(['tom', 10], index=['name', 'score']), 
    pd.Series(['nick', 15], index=['name', 'score']),
    pd.Series(['juli', 14], index=['name', 'score']),
]
pd.DataFrame(data)
# 출력
 	name 	score
0 	tom 	10
1 	nick 	15
2 	juli 	14
```

<br>

##### iii. NumPy Array로

```python
df = pd.DataFrame(np.random.randn(5, 3), columns=list('ABC'))
df
# 출력
 	A 			B 			C
0 	-0.208920 	0.723887 	-0.290097
1 	0.536449 	0.168869 	1.537196
2 	0.503892 	0.126006 	-0.454374
3 	-0.266239 	-0.048982 	-0.196954
4 	-0.193741 	-1.117400 	-0.133509
```

<br>

##### iv. csv 파일로

- csv 파일이란 comma-separated values 파일로써 콤마로 값들이 나눠져있는 파일을 의미한다.
- [titanic.csv](https://github.com/pandas-dev/pandas/blob/master/doc/data/titanic.csv)를 사용하였다.

```python
titanic_df1 = pd.read_csv('./titanic.csv')
titanic_df1.head()
```

**출력**

|      | PassengerId | Survived | Pclass | Name                                              | Sex    | Age  | SibSp | Parch | Ticket           | Fare    | Cabin | Embarked |
| ---- | ----------- | -------- | ------ | ------------------------------------------------- | ------ | ---- | ----- | ----- | ---------------- | ------- | ----- | -------- |
| 0    | 1           | 0        | 3      | Braund, Mr. Owen Harris                           | male   | 22.0 | 1     | 0     | A/5 21171        | 7.2500  | NaN   | S        |
| 1    | 2           | 1        | 1      | Cumings, Mrs. John Bradley (Florence Briggs Th... | female | 38.0 | 1     | 0     | PC 17599         | 71.2833 | C85   | C        |
| 2    | 3           | 1        | 3      | Heikkinen, Miss. Laina                            | female | 26.0 | 0     | 0     | STON/O2. 3101282 | 7.9250  | NaN   | S        |
| 3    | 4           | 1        | 1      | Futrelle, Mrs. Jacques Heath (Lily May Peel)      | female | 35.0 | 1     | 0     | 113803           | 53.1000 | C123  | S        |
| 4    | 5           | 0        | 3      | Allen, Mr. William Henry                          | male   | 35.0 | 0     | 0     | 373450           | 8.0500  | NaN   | S        |

```python
titanic_df2 = pd.read_csv('./titanic.csv', header=None)
titanic_df2.head()
```

**출력**

|      | 0           | 1        | 2      | 3                                                 | 4      | 5    | 6     | 7     | 8                | 9       | 10    | 11       |
| ---- | ----------- | -------- | ------ | ------------------------------------------------- | ------ | ---- | ----- | ----- | ---------------- | ------- | ----- | -------- |
| 0    | PassengerId | Survived | Pclass | Name                                              | Sex    | Age  | SibSp | Parch | Ticket           | Fare    | Cabin | Embarked |
| 1    | 1           | 0        | 3      | Braund, Mr. Owen Harris                           | male   | 22   | 1     | 0     | A/5 21171        | 7.25    | NaN   | S        |
| 2    | 2           | 1        | 1      | Cumings, Mrs. John Bradley (Florence Briggs Th... | female | 38   | 1     | 0     | PC 17599         | 71.2833 | C85   | C        |
| 3    | 3           | 1        | 3      | Heikkinen, Miss. Laina                            | female | 26   | 0     | 0     | STON/O2. 3101282 | 7.925   | NaN   | S        |
| 4    | 4           | 1        | 1      | Futrelle, Mrs. Jacques Heath (Lily May Peel)      | female | 35   | 1     | 0     | 113803           | 53.1    | C123  | S        |

```python
titanic_df3 = pd.read_csv('./titanic.csv', index_col=2)
titanic_df3.head()
```

**출력**

|        | PassengerId | Survived | Name                                              | Sex    | Age  | SibSp | Parch | Ticket           | Fare    | Cabin | Embarked |
| ------ | ----------- | -------- | ------------------------------------------------- | ------ | ---- | ----- | ----- | ---------------- | ------- | ----- | -------- |
| Pclass |             |          |                                                   |        |      |       |       |                  |         |       |          |
| 3      | 1           | 0        | Braund, Mr. Owen Harris                           | male   | 22.0 | 1     | 0     | A/5 21171        | 7.2500  | NaN   | S        |
| 1      | 2           | 1        | Cumings, Mrs. John Bradley (Florence Briggs Th... | female | 38.0 | 1     | 0     | PC 17599         | 71.2833 | C85   | C        |
| 3      | 3           | 1        | Heikkinen, Miss. Laina                            | female | 26.0 | 0     | 0     | STON/O2. 3101282 | 7.9250  | NaN   | S        |
| 1      | 4           | 1        | Futrelle, Mrs. Jacques Heath (Lily May Peel)      | female | 35.0 | 1     | 0     | 113803           | 53.1000 | C123  | S        |
| 3      | 5           | 0        | Allen, Mr. William Henry                          | male   | 35.0 | 0     | 0     | 373450           | 8.0500  | NaN   | S        |

- pandas.read_csv 함수를 사용하면 문자열 형태의 파일 경로를 인자로 하여 DataFrame을 만들 수 있다. [reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html?highlight=head#pandas.DataFrame.head)
- pandas.DataFrame.head 는 DataFrame의 상위 항목 몇 개를 반환한다.
  - DataFrame.head(*n=5*) [reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html?highlight=head#pandas.DataFrame.head) [source](https://github.com/pandas-dev/pandas/blob/v1.1.1/pandas/core/generic.py#L4633-L4703)
- header 인자를 통해 csv파일의 가장 첫 줄을 DataFrame의 columns 라벨로 할지 정할 수 있다.
- index_col 인자를 통해 몇 번째 column을 index로 할지 정할 수 있다.

<br>

<br>

<br>

<br>

참고문서

- [Pandas Documentation](https://pandas.pydata.org/docs/index.html)
- [GeeksforGeeks](https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/?ref=rp)
- [RIP Tutorial](https://riptutorial.com/ko/pandas/example/5175/numpy%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC-%EC%83%98%ED%94%8C-dataframe-%EB%A7%8C%EB%93%A4%EA%B8%B0)

