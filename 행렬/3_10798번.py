# A~Z, a~z, 0~9
# 한줄의 단어 max 15개까지, 각 줄의 단어 개수는 다를 수 있음 
# 빈칸이 있는 경우 넘어가고 그 아래 단어를 읽는다
# 위 과정을 띄어쓰기 없이 쭉 출력해라 

matrix = [input() for _ in range (5)] 
#문제 1. 입력이 공백으로 주어지지 않는다.
# 15* 15 matrix 탐색한다음에 공백은 제거하면 되는거 아닌가? 5개의 행의 max값 구해서 max*5 matrix 로 풀자 

# max_len = 0
# for row in matrix: 
#     new_len = len(row) 
#     if new_len >= max_len:
#         max_len = new_len
#line10 ~ lin14까지의 코드를 아래 한줄로 줄일 수 있다. 
max_len = max(len(row) for row in matrix) #제네레이터 표현식 
output = ''
for col in range(max_len):
    for row in range(5):   
        if col < len(matrix[row]):  #해당 행의 길이보다 현재 체크하는 col이 작을때ㅁ나 
            output += matrix[row][col]
print(output)


#파이썬에서 리스트를 문자열로 일정하게 합쳐줌 > '구분자'.join(리스트)
