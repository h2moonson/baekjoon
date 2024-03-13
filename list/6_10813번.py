# N개의 바구니 바구니 번호 = 공번호 
# 공을 바꿀 바구니 2개 임의 선택 > 공 교환 
# 공을 어떻게 바꿀지가 주어졌을때, M번 공을 바꾼 이후에 바구니에 맞는 공 
# 1. N 과 M이 주어짐 N개의 바구니, M 번 바꿀것 
# 2. 그 다음 줄에 i, j입력 ( 서로 바꿀 바구니 )
N,M = map(int, input().split())
baskets = []
for i in range (1,N+1):
    baskets.append(i)

for num in range (M): 
    i,j = map(int, input().split())
    temp = baskets[i-1]
    baskets[i-1] = baskets[j-1]
    baskets[j-1] = temp

for i in range (len(baskets)):
    print(baskets[i], end=" ")
    if i==len(baskets)-1:
        print(" ")
print(*baskets) #한줄 출력가능 
print(*sorted(baskets))
