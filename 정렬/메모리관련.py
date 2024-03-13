#https://wikidocs.net/21057

#메모리 주소 알아내기 
>>> id(2)
4484212032

#가비지컬렉션 : 파이썬은 불필요한 객체를 자동으로 삭제함
#별도로 관리할 필요는x, 굳이 GC관련된 기능 써야한다면 import gc 
#그러나 비추 

#성능향상과 메모리 잘 쓰는 법 
#대부분의 프로그래밍 언어가 느려지는 이유 : 메모리가 재할당이 이루어지기 떄문 
#주로 for 문에서 발생 

#case 1) 중첩 for 문 
import time

start_time = time.time()
a = list(range(100000))
a2 = list()

for i in a:
    a2.append(i*2)

end_time = time.time() 
fin = end_time - start_time
print(fin)
#결과
0.04319477081298828
# a2 변수에 append하기에 메모리 재할당이 일어남
# 느리다. 

#case2) 리스트 컴프리헨션 방식 > 속도 조금 개선
import time

start_time = time.time()
temp = [x*2 for x in range(100000)]
end_time = time.time()
fin = end_time - start_time
print(fin)
#결과
0.01129007339477539

#case3) map()함수 사용. lambda 함수 

import time

start_time = time.time()
a = list(range(100000))
a2 = map(lambda n: n*2, a) 
import time

start_time = time.time()
a = list(range(100000))
a2 = map(lambda n: n*2, a)
end_time = time.time()

fin = end_time - start_time
print(fin)
#결과
0.0034818649291992188

end_time = time.time()

fin = end_time - start_time
print(fin)
#결과
0.0034818649291992188
