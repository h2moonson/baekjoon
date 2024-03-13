#  N*M 행렬 입력, 맨 첫줄에는 N과 M이 주어짐 
N, M = map(int, input().split())
first =[list(map(int , input().split())) for _ in range (N)]
second=[list(map(int , input().split())) for _ in range (N)]
for i  in range (N):
    for j in range(M):
        print(first[i][j] + second[i][j], end=" ") #아니면 리스트에 append해도 됨 
    print("")

# 풀이 2 
import numpy as np

N, M = map(int, input().split())
first = np.array([list(map(int, input().split())) for _ in range(N)])
second = np.array([list(map(int, input().split())) for _ in range(N)])

result = first + second
for row in result:
    print(' '.join(map(str, row))) #join메서드 _ row의 요소를 공백으로 구분해서 합침 