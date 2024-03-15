import sys
index=[0]*10
#number = input()
number = (sys.stdin.readline().strip())
#그러나, readline() 함수로 읽어온 문자열은 개행 문자(\n)도 
#포함하므로 이를 제거하고 변환해주어야 합니다.

for num in number: 
    # print(num)
    index_= int(num)
    index[index_]+=1
for i in range(9,-1,-1): #역순으로 
    
    if index[i]!=0:
        for j in range(index[i]):
            print(i,end="")
print("")

#2 @@@@sort메서드 사용 
n = int(input())
 
li = []
for i in str(n):
    li.append(int(i))
# li = list(map(int,str(n))) 으로 변경가능
    
li.sort(reverse=True) # 내림차순
 
for i in li:
    print(i,end='')

#1의 조금 더 간단한 버전 
import sys

index = [0] * 10

number = sys.stdin.readline().strip()

for num in number: 
    index[int(num)] += 1

for i in range(9, -1, -1): 
    print(str(i) * index[i], end="")

print("")  # 마지막에 개행 문자를 출력하여 한 줄을 끝냄

