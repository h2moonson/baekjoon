# 9*9 격자판에 81개의 자연수 또는 0이 주어질 때
# 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한
# 수인지 구하는 프로그램을 작성하시오 
sample_matrix = [list(map(int, input().split())) for row in range (9)]

# for row in range (len(sample_matrix)):
#     for col in range (len(sample_matrix[row])): 
#         print(row, col, sample_matrix[row][col])
max = 0 #자연수 또는 0이 주어진다. 모든격자가 0이라면 max가 업뎃이 안됨 
index = (0, 0) 
for r, row in enumerate(sample_matrix):
    for c, letter in enumerate(row):
        if letter >= max: 
            max = letter 
            index = (r+1, c+1)
print(max)
for i in index: print(i, end=" ")