# #N개의 숫자가 공백없이 쓰여있다, 이 숫자를 모두 합해라
# N=int(input())
# number=input()
# sum = 0
# for i in range (N):
#     sum += int( number[i])
# print(sum)

#제너레이터 표현식 코드, 제너레이터 표현식을 인자로 전달 가능 
# 리스트를 생성하는 대신, 한번에 하나의 항목을 생성하는데 사용됨 
N=int(input())
number=input()
tot_sum = sum(int(digit) for digit in number)
#tot_sum = sum([int(digit) for digit in number]) 얘도 가능은 한데 메모리 측면에서 비효율
print(tot_sum)

squares = [x**2 for x in range(1, 6)]
print(squares)
# 출력: [1, 4, 9, 16, 25]