# 4개의 x,y 좌표 
# 가장 max y 좌표 - min y 좌표
# 가장 max x 좌표 - min x 좌표 

x = []
y = []
N = int(input())
for _ in range (N):
    A, B = map(int, input().split())
    x.append(A); y.append(B)
    
possible_size = []
possible_size.append(max(x)-min(x))
possible_size.append(max(y)-min(y))
area = possible_size[0] * possible_size[1] 
print(area) 
