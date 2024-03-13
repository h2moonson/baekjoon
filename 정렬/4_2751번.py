import sys
N= int(input())
numbers = [int(sys.stdin.readline()) for _ in range (N)]
#반복문안에서의 input()은 많은 시간 소요 
numbers.sort()
for num in numbers: 
    print(num)