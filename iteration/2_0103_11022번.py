T=int(input()) #몇 번 반복할 것인지 선택 
for i in range(1, T+1):
    A,B=map(int,input().split())
    print(f"Case #{i}: {A} + {B} = {A+B}")
