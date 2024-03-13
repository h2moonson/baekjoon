#중앙에서 N번방 까지 최소개수의 방을 지나서 갈때 몇개의 방을 지나서 가는가? 
N = int(input())
step = N //6
num=1
i = 1
while num < N : 
    num += 6*i
    i+=1
print(i) 
#1
#6개 > 몫이 0 인경우 step +1 
#8~19 = 12개 > 몫이 1인 경우 +2 
#20~37 = 18개