# liam > 0.5달러 줘야하는데 5달러주는 미친알바생
# 거스름돈의 액수 tot이 주어지면 
# 거슬러 줘야할 
# Quarter ($0.25), Dime($0.10), Nickel($0.05), Penny($0.01)개수를 해라 
# 거스름돈은 항상 $5.00 이하이고, 손님이 받는 동전의 개수를 최소로 해야함 

# 첫째줄에 테스트 케이스의 개수 T가 주어짐 
# 3
# 124
# 25
# 194

# 4 2 0 4
# 1 0 0 0
# 7 1 1 4
T = int(input())
change_list=[25,10,5,1]

change = []
for i in range(T): 
    test = []
    for j in range (4): 
        test.append(0)
    change.append(test)

#change2 = [[0 for _ in range (4)] for _ in range (T)] #한줄로 그냥 생성 가능 
#print(change2)

order = [int(input()) for _ in range (T)] 

for i in range (T): 
    for j in range (4):
        coin= change_list[j]
        change[i][j]= (order[i] // coin)
        order[i] %= coin

for result in change: 
    print(*result)