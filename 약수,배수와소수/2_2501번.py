N, K = map(int, input().split())
factor = [ i for i in range (1, N+1) if N % i == 0]

#modified_factor = list(set(factor)) #리스트에서 중복 요소 제거 
if len(factor) < K:
    print(0)
else:
    print(factor[K-1])