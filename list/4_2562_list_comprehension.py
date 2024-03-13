#리스트 컴프리헨션 코드
numbers=[int(input()) for _ in range(9)]
print(max(numbers))
print(numbers.index(max(numbers))+1)