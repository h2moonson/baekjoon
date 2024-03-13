def f_function (a1,a0, num):
     result = a1*num + a0
     return result 

def g_function(c,num):
     result = c*num #big O notation 에 의해 수행시간 g(n)= n
     return result
a1, a0 = map(int, input().split()) #얘내는 음수조건도 있음
#따라서 조건 하나 더 추가 둘다 양수 일때는 왼쪽조건
#f_fuction이 음수라면 n을 1로 두면 f값은 a1+a0 , g은 c값임 g의 min값은 
#c가 1일 때임 따라서 a0가 0이라고 했을 떄 a1<=c값
#너무 복잡하게 생각말고 그냥 반례찾는다고 생각 
c = int(input())
n0 = int(input())
if f_function(a1,a0,n0)<=g_function(c, n0) and (a1<=c): 
     print(1) 
else:
     print(0)


