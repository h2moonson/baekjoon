# N 킬로 그램 배달 
# 18 kg = 5 * 3 + 3 * 1 이 가장 적은 
# 5*x + 3* y  = N 의 방정식의 해 중에서 합이 최소인 것을 구하는 문제 
# 브루트 포스로 해결하면 easy

N = int(input())
x_max = N // 5 
y_max = N //3 
size = []


for x in range(x_max+1):
    for y in range (y_max+1) :
        if 5 * x  + 3 * y == N : 
            size.append(x+y)

if len(size)!= 0:
    print(min(size))
else: 
    print(-1)
