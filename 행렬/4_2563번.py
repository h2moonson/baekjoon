# 가로세로 100, 100 흰색 도화지
# 가로 세로 크기가 각각 10 10인 정사각형 검은 도화지
# 색종이를 한장 혹은 여러장 붙인 후 검은 영역 부분의 넓이 구하기 
# 첫 줄에 붙일 색종이의 개수 

matrix = []
for row in range (10):
    test  = [] #새로운 행 생성
    for col in range (10): 
        test.append(None) 
    matrix.append(test)
print(matrix) 
# 6~12 : 이중 for문을 활용한 matrix 생성 

rows = 100
cols = 100
matrix2 = [[None for col in range(cols)] for row in range(rows)]
n = int(input())
for _ in range (n): 
    lat ,long  = map(int, input().split())
    for row in range (lat,lat+10): 
        for col in range (long, long+10):
            matrix2[row][col] = 1 
area = 0
for row in range (rows):
    for col in range(cols):
        if matrix2[row][col] == 1: 
            area +=1 
print(area)

#18부터 29번 라인을 집합으로 처리할 수  있음
n = int(input())
updated_cells = set()

for _ in range(n):
    lat, long = map(int, input().split())
    for row in range(lat, lat + 10):
        for col in range(long, long + 10):
            updated_cells.add((row, col)) #이 과정에서 이미 추가된 셀은 더하지 않음 

area = len(updated_cells)
print(area)
