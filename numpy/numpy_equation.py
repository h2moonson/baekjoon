import numpy as np

a = np.array( [20,30,40,50] )
b = np.arange( 4 ) # [0 1 2 3] 생성 
print("배열 a", a)
print("arrange로 생성한 b",b)  
c = a-b 
# 기본적으로는 요소별 연산이다. @또는 dot 함수를 사용해서 matrix multiplication 가능 
print("c=a-b 의 결과값",c)
print("b**2 의 결과값",b**2)
print("a의 sine값 * 10 의 결과값",10*np.sin(a))
print("a가 35보다 작은지에 대한 비교 결과",a<35)

AA = np.array( [[1,1],
                [0,1]] )
BB = np.array( [[2,0],
                 [3,4]] )
print("AA * BB 의 결과값\n",AA * BB)
print("AA @ BB 의 결과값\n",AA @ BB)
print("AA.dot(BB) 의 결과값\n",AA.dot(BB))

'''
배열 a [20 30 40 50]
arrange로 생성한 b [0 1 2 3]
c=a-b 의 결과값 [20 29 38 47]
b**2 의 결과값 [0 1 4 9]
a의 sine값 * 10 의 결과값 [ 9.12945251 -9.88031624  7.4511316  -2.62374854]
a가 35보다 작은지에 대한 비교 결과 [ True  True False False]
AA * BB 의 결과값
 [[2 0]
 [0 4]]
AA @ BB 의 결과값
 [[5 4]
 [3 4]]
AA.dot(BB) 의 결과값
 [[5 4]
 [3 4]]


'''