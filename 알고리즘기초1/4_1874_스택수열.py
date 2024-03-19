#Last In First Out 구조 
# [4, 3, 6, 8, 7, 5, 2, 1]
# push하는 순서 반드시 오름차순> push 연산은 + pop연산은 -
n = int(input())
sequence = [int(input()) for _ in range (n)]
# 1 , 2 ,3 ,4
# [4,3 ]pop2번
# 1, 2, 5, 6
# [4, 3, 6] # pop1번
# 1, 2, 5, 7, 8 
# [4, 3, 6, 8, 7 ,5, 2,1] #pop4번 
for i in range (n-1): 
    pivot = sequence[i]
    cnt = 0
    for j in range (i+1, n):
        if pivot >= sequence[j]:
            cnt+=1
    if cnt == 0:
        print(pivot)
        print("NO")
        break
num = 1 
test_stack = []
for i in range (n):
    while num <= sequence[i]: 
        print("+")
        test_stack.append(num)
        num+=1
        print(test_stack)
    if num == sequence[i]: 
        if test_stack.find(sequence[i+1]):
            while num >= sequence[i+1]:
                print("-")
                test_stack.pop()
    print(test_stack)