N = int(input())
numbers = [int(input()) for _ in range (N)]
numbers.sort()
#sorted()는 새로 정렬한 리스트 반환 
#sort는 
for num in numbers:
    print(num)