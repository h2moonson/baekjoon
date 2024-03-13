N = int(input())
# i = 2
# while N >= i: #소인수 분해 하는 수보다 크거나 같을 때까지
#     if N % i== 0:  #나누어 떨어지는 경우 
#         print(i)
#         N//=i #N을 업데이트 한다.
#     else : 
#         i+=1 
#     if i > N:
#         #print(f"탈출 조건 {i} > {N}")
#         break

# 풀이 2 
    
for i in range (2,N+1):
    if N % i == 0 :
        while N % i == 0:
            print (i)
            N /= i
