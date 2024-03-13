N = int(input())
test_list = map(int, input().split())
decimal = N
for num in test_list: 
    if num == 1 : 
        decimal -=1
    
        #print("1이어서 다음으로")
        continue  
    for i in range (2, int(num**0.5) + 1): # 제급근까지만 확인하면 됨 
        # 1인 조건을 같이 넣으면 range(2, int(num**0.5) + 1)가 range(2, 2)가 되어 실행이 안됨
        if num % i == 0: 
            decimal -= 1 
            #print("if 문 안에 들어와서 빠짐", num)
            break 

print(decimal)