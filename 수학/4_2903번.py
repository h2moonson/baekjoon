# 중앙이동 알고리즘 
# 그냥 정사각형 크기 구하는 문제 
N = int(input()) 
size=2
for i in range (1, N+1): 
    dots= (size + (size-1))**2
    size = 2*size - 1
print(dots)