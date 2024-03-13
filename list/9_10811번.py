#N개의 바구니, M번 reverse 할 것, i~j 까지 뒤집음
N, M = map(int,input().split()) 
basket = [x for x in range (1, N+1)]
# for _ in range (M): 
#     i, j = map(int, input().split())
#     test1 = basket[i-1: j:1].reverse()#reversed 는 역방향 반복자를 반환 
#     test2 = basket[j: len(basket) :1] #리스트[start: stop: step]
#     basket = test1.extend(test2)

# @@ NoneType오류가 반환되는 이유! reverse와 extend 모두 리스트 변경 후에 None을 반환 
for _ in range (M):
    i, j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

print(*basket)