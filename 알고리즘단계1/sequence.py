n = int(input())
# [4 3 6 8 7 5 2 1]
sequence = [int(input()) for _ in range (n)]
sequence2 = []
num = 0

test_stack = []

append_pop_history = []
for i in range (n):
    while num < sequence[i]:
        #print("+")
        append_pop_history.append("+")
        num+=1 # 1이어도 0에서 시작, while문에 들어오고 1로 변하고 append
        test_stack.append(num)

        #print(test_stack)
    # if num == sequence[i]: #이제 같아진 경우 언제까지 pop할지 선택
    #     finish_flag = False
    #     pop_i = i # 전체 시퀀스 i를 저장 
    #     sequence2.append(test_stack.pop())
    #     #print("-") # 맨 위에꺼 일단 뺌
    #     append_pop_history.append("-")
    #     while not finish_flag and pop_i+1 <n and test_stack: 
    #         if test_stack[-1] == sequence[pop_i+1]: 
    #             sequence2.append(test_stack.pop())
    #             #print("-") #이때 3빠짐
    #             append_pop_history.append("-")
    #             pop_i+=1
    #         else: finish_flag = True 
        
    # 플래그 없애고 개선한 코드 아래와 같음 
    if test_stack and test_stack[-1] == sequence[i]:
        pop_i = i
        while test_stack and pop_i < n and test_stack[-1] == sequence[pop_i]:
            sequence2.append(test_stack.pop())
            append_pop_history.append("-")
            pop_i += 1

flag= 1
while test_stack: 
    #print("-")
    append_pop_history.append("-")
    sequence2.append(test_stack.pop())

for i in range (n):
    if sequence[i] == sequence2[i]:
        pass
    else: 
        #print("불일치")
        flag = 0

if flag: 
    for char in append_pop_history:
        print(char)
else: 
    print("NO")
