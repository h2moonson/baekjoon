# 두 수가 주어졌을 때, 3가지 case중 어떤 것인지를 구하는 프로그램을 작성
while True : 
    A, B = map(int, input().split())
    if A ==0 and B == 0: 
        break
    match (A % B, B % A): 
        case (_,0):
            print("factor")
            #print("첫번째 숫자가 두 번째 숫자의 약수이다.")
            
        case (0, _):
            print("multiple")
            #print("첫번째 숫자가 두 번째 숫자의 배수이다.")
        case _ : 
            print("neither")
            #print("아무 것도 아닙니다. ")
 
# # match_case 구문이 유용한 경우 
# for n in range(1, 101):
#     match (n % 3, n % 5): #튜플로도 여러가지 조건 나타낼 수 있다(?)
#         case (0, 0):
#             print("FizzBuzz")
#         case (0, _): # _ 는 아무 값이나 상관 없다는 뜻이다. 
#             print("Fizz")
#         case (_, 0):
#             print("Buzz")
#         case _:
#             print(n)


    