N, K = map(int, input().split())
#원형큐?
#1  4  인덱스를 구현해라 K번째 사람. 예를 들어 2명남았을 때 3번째 사람이면 3 % len(list) 
#인덱스 0번부터 시작하니깐 -1
circle = [str(i) for i in range (1,N+1)]  
permutation = []
del_index = K - 1 # 여기서 처음 시작 할 때 0으로 맞춰주면 편하다!! 
while circle: 
    del_index = (del_index % len(circle))
    permutation.append(circle.pop(del_index))
    del_index = del_index + K - 1

str= ", ".join(permutation)
print("<"+str+">")
# 1 2 3 4 5 6 7 