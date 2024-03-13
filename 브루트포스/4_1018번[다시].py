n, m = map(int,input().split())
chess = [input()for _ in range(n)]

w = 'W', 'B'
b = 'B', 'W'

def check(i,j):
    result_w=0
    result_b=0 
    for di in range (8): # di dj는 인덱스의 차이
        for dj in range (8): 
            ni, nj = i+di, j+dj # ni nj 는 현재 인덱스
            if chess[ni][nj] != w[(di+dj)%2]: #왼쪽 위 시작 색상이 화이트라고 했을 때
                #인덱스 합이 짝수인만큼 떨어진 애들은 흰색이어야함 
                result_w+=1
            if chess[ni][nj] != b[(di+dj)%2]: #왼쪽 위 시작 색상이 블랙기준으로 칠한다 했을떄
                result_b+=1
    return min(result_w, result_b)

result= 10000000
for i in range(n-7):
    for j in range(m-7):
        result = min(result, check(i,j)) #계속에서 result의 min을 업데이트

print(result)

for i in range (0, n-7):
    for j in range(0, m-7):
        start_was_white = 0
        start_was_black = 0 

        for x in range (i, i+8):
            for y in range (j, j+8):
                if (x+y)%2 ==0: #인덱스의 합이 짝수인경우 
                    #  @@start_was_white부터 생각해보자
                    if chess[x][y]!= 'W':
                        start_was_white +=1 #화이트 여야 하는데 검정이니 

                else: 
                    if chess[x][y]!= 'B':
                        start_was_white +=1 #블랙이어야 하는데 흰색이니깐 
 # 3/11 reivew @@@@@@@@이렇게 한가지 case만 잡고 흐름잡아가면 쉽다
#자꾸 올바른 케이스 상상하지 말고, 틀린 케이스 즉 카운트 변수 증가하는 경우만 따라가자 