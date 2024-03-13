import numpy as np 
a= np.array([1,2,3])
b= np.array([[1,2,3],[4,5,6]])
print(a)
print(b)
'''
출력: 
[1 2 3]

[[1 2 3]
 [4 5 6]]
'''
# linspace = linear space : 선형적으로 변하는 row vector

c = np.linspace(0, 1, 6) # start, end, num-point
# 0에서 1까지 균등하게 6개의 포인트로 나눔> 0.2 간격 
d = np.linspace(0, 1, 5, endpoint=False) 
# endpoint = False? 끝점을 포함하지 않는다. > 6개라고 생각하면 됨  0.2 간격 