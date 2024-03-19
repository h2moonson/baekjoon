n = int(input())
# [4 3 6 8 7 5 2 1]
sequence = [int(input()) for _ in range (n)]
# 1 2 3 4 
# [4 3 ]pop 2번
# 1 2 5 6
# [4 3 6] #pop 1번 
# 1 2 5 7 8 
# [4 3 6 8 7 5 2 1]
finish_flag = False
for i in range (n-1):
    if not finish_flag:
        pivot = sequence[i]
        cnt = 0
        for j in range (i+1, n-1):
            if pivot >= sequence[j]:
                cnt+=1
            if cnt == 0:
                #print(pivot)
                print("NO")
                finish_flag = True
                break
    else: 
        break
num = 0
test_stack = []
for i in range (n):
    while num < sequence[i]:
        print("+")
        num+=1 # 1이어도 0에서 시작, while문에 들어오고 1로 변하고 append
        test_stack.append(num)
        #print(test_stack)
    c_seq = i
    if num == sequence[i]: #이제 같아진 경우 언제까지 pop할지 선택
        next = sequence[i+1] #다음 수열에 있는 애로 검사 

        tgt = 0
        for i, x in enumerate(test_stack):
            if x == next: 
                tgt = i #인덱스 설정하고 break
                break
        for i in range (c_seq - tgt): 
            test_stack.pop()
            print("-")
while test_stack: 
    print("-")
    test_stack.pop()