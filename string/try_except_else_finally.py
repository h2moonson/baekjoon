# try:
#     #예외가 발생할 수 있는 코드
# except 예외타입:
#     #예외 발생 시 실행할 코드
# else:
#     #예외가 발생하지 않았을 때 실행할 코드
# finally: 
#     #예외 발생 여부와 관계없이 항상 실행할 코드 
try:
    num1=int(input("첫번째 숫자를 입력하세요: "))
    num2=int(input("두번째 숫자를 입력하세요: "))
    result= num1/num2
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else: 
    print("결과: ", result)
finally:
    print("저는 무조건 실행됨 ")