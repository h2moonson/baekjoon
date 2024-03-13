num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 10진법을 B진법으로 변환 
sample_queue = []
N, b = map(int, input().split()) #10진수 입력받기
# while True: 
#     remainder = N % b
#     sample_queue.append(remainder)
#     if N < b: # 몫이 나누는 수보다 클 때만 
#         break
#     N = N //b # 몫

# #print(sample_queue)
# value = []
# for key in sample_queue[::-1]: #다시 앞에서 부터
#     value.append(num_list[key]) 
#     #print("for 문 도는 중")
# print("".join(value))

#아래처럼 하면 훨씬 간단하다 
s = ""
while N: #N값이 0이 될 때까지 반복 > 몫이 0이되면 자동으로 끝나도록 
    s+=str(num_list[N%b])
    N //=b
print(s[::-1])