import sys
N = int(input())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
numbers.sort()
# numbers.sort(reverse = True)
for num in numbers:
    print(num)

#메모리 초과에 관련된 문제 > 공간 복잡도를 줄여야한다. 
#계수정렬 : count할 배열 선택하고 , 각 요소별로 몇개가 있는지 인덱스에 담음
# 데이터의 크기가 한정되어 빠르게 동작해야할 때 사용됨
N = int(sys.stdin.readline())
arr = [0]*10001
for _ in range(N): 
    num = int(sys.stdin.readline())
    arr[num] +=1 #arr[num]에 num이 들어온 개수 count 
for i in range(10001):
    if arr[i]!=0:
        for j in range(arr[i]):
            print(i)
