N,M=map(int,input().split())
basket=[0]*N
print(basket)

for i in range (M):
    start,end,number=map(int,input().split())
    for j in range (start,end+1):
        basket[j-1]=number
    
print(" ".join(map(str,basket)))#리스트 원소가 정수이므로 변환해줘야함
'''
3 3 0 0 0
3 3 4 4 0
1 1 1 1 0
1 2 1 1 0
'''