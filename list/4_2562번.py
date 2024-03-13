list=[]
for i in range(9):
    list.append(int(input()))

max=0
i=0
max_turn=0
for num in list:
    i+=1
    if num>max:
        max=num
        max_turn=i
    else:
        pass

print(max)
print(max_turn)

#리스트 컴프리헨션 코드
numbers=[int(input()) for _ in range(9)]
print(max(numbers))
print(numbers.index(max(numbers))+1)