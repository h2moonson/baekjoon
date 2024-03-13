#1. 리스트 컴프리헨션
#정수를 문자열로 변환 후에 for문 이용해서 리스트로 변환
def solution (n):
    return sum([int(i) for i in str(n)]) 

#2. 재귀함수를 이용
def sum_digit (number):
    if number < 10:
        return number
    return (number % 10) + sum_digit(number // 10)

# 6543이 number로 들어왔다고 하면,
# 1) 3 + sum_digit(654)
# 2) 4 + sum_digit(65)
# 3) 5 + sum_digit(6)
# 4) return 6
# 따라서 3 4 5 6이 순서대로 합해지게 된다.

#3. map + sum 메서드 
def sum_digit (number):
    return sum(map(int,str(number)))