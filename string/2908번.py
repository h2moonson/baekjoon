#734와 893이 주어졌을 때 상수의 대답을 출력해라 
A, B=input().split()

A = int(A[::-1])
B = int(B[::-1])
print(A if A>B else B)

# if A>B:
#     print(A)
# else: 
#     print(B)