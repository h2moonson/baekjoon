#B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오 
#A: 10, B:11, ... , Z: 35
#10~ 35까지의 알파벳에 대한 수 정의를 먼저 해줘야겠다.
N, B = input().split()
B = int(B)
#ZZZZZ인 경우, 
dict={}
alphabet = 65
for num in range (10, 36): 
    dict[chr(alphabet)] = num
    alphabet+=1
#print(dict)
result = 0
for i in range (len(N)):
    try:
        p = int(N[i])
    except: 
        #print("10진법을 넘어가는 숫자 발생,p값은 ",dict[N[i]])
        p = dict[N[i]]
    
    result += p*B**(len(N)-1-i)
print(result)
   

#enumerate 함수를 이용한 풀이 
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = input().split()
answer = 0
for i, num in enumerate(n[::-1]):
    answer += (int(b) ** i) * num_list.index(num)
print(answer)