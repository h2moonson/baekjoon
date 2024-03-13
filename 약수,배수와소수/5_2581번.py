M = int(input())
N = int(input())
decimal = 0
decimal_list = [num for num in range (M, N+1)]
delete_required = []
#print(decimal_list)
for num in range (M, N+1):
    if num == 1 : 
        #print("1이어서 다음으로")
        decimal_list.remove(num)
        continue  
    #print("line 11")
    for i in range (2, int(num**0.5) + 1): # 제곱근까지만 확인하면 됨 
        if num % i == 0: 
            #print("소수아님", num)
            delete_required.append(num) #리스트를 반복하면서 제거하려고 하면 문제 발생
            break
for dec in delete_required: 
    decimal_list.remove(dec) 
if len(decimal_list) == 0 :
    print(-1)
else: 
    print(sum(decimal_list))
    print(min(decimal_list))
