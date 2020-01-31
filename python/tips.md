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