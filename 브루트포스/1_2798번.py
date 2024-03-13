#블랙잭 : 카드 합이 21넘지 않는 한도 내에서 카드의 합max
#각 카드에는 양의 정수. 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에
#이후 딜러가 숫자 M을 크게 외침

#플레이어 > N장의 카드 중 장 고르기 
N, M = map(int, (input().split())) 
deck = []
deck = list(map(int, input().split()))
#print(deck)


tot = 0 
for num1 in range (N):
    for num2 in range (num1+1,N):
        for num3  in range (num2+1, N):
            sum = deck[num1] + deck[num2]  + deck[num3] 
            if sum > tot and sum <= M: 
                tot = sum
                #print("업뎃 행중, 값: ", sum)
            else: 
                sum = tot 


print(sum)
    
            
