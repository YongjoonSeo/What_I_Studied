# tips



1. **list 그냥 글자로 프린트 하고 싶을 때 언패킹 가능.**
   **--> b = [1,2,3,4,5,6] , print(b)
   --> 1 2 3 4 5 6
   print 언패킹 할 때 attribute중에 sep이 있다 (나누는 거 어떤 식으로 할지)
   print(b, sep=',')**
   **--> 1,2,3,4,5,6**

2. 변수 이름 좀 더 가독성있게 짜보자.
   stu = list(map(int, input().split())) 대신에
   gen, k = map(int,input().split()) 이런 식으로 하면 사용하기도 더 괜찮다.

3. ```python
    for _ in range(N):
      print(field[_])
    ```

  ==> 내가 구상한 리스트의 형태로 나오는지 체크할 수 있음. 주석 처리 해두고 중간중간에 틀리는지 체크.


4. 정수 입력 받을 때 올림 쉽게 할 수 있는 방법: N+K-1 // K



5. 평면으로 표현할 때, 항상 x, y는 설계대로 해놓고 index에 x,y를 반대로 넣는다고 생각하자.



6. 1차원 배열은 table, 2차원 배열은 field로 네이밍하면 편하다.



7. ```python
   import sys
   input=sys.stdin.readline
   
   for _ in range(int(input())):
       a, b = map(int, input().split())
       print(a+b)
   ```

   이런 식으로 함수 이름에 덮어버려도 작동한다.