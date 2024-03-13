#첫째 줄에 N이 주어지고 
#2*N -1 번째 줄까지 별 출력 9개 
#N번째 줄에 max 출력 
#빈칸 [4,1] , 3 -2 , 2 -3 , 1- 4, [0,5]
N = int(input())
result=[]
for i in range (N-1):
    result.append(" "*(N-1-i) + "*"*(2*i+1))
    print(result[i])
print("*"*(2*N-1))
for i in range(N-1):
    print(result[N-2-i])

N = int(input())
for i in range(1,N):
    print(" "*(N-i)+"*"*(2*i-1))
for i in range(N,0,-1): #N에서 0이전(1까지)감소하는 방향으로
    print(" "*(N-i)+"*"*(2*i-1))