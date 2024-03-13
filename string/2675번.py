T=int(input()) #몇번 입력받을 것인가
result=[]
for i in range(T):
    R, S = input().split()
    R = int(R)
    new_S = [S[num]*R for num in range (len(S))]
    new_S = ''.join(new_S) #구분자.join(리스트) ,split함수의 역이라고 생각해라 
    # 6,7번을 한줄로 처리 가능한 라인 
    new_S = ''.join([char*R for char in S])
    
    result.append(new_S)
# for i in range (len(result)):
#     print(result[i])
[print(res) for res in result] #단점, 리스트가 생성이 되어버럼 
# Case = int(input())

# for i in range(Case):
#     N, S = input().split()
#     for j in range(len(S)):
#         print(S[j] * int(N), end = '')
#     print('')