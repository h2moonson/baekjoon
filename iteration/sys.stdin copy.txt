import sys

#중요한 차이점은 input() 함수는 한 번에 한 줄의 입력을 받고, 
#sys.stdin을 사용하면 여러 줄의 입력을 받을 수 있다는 것입니다. 
#따라서 입력의 종류와 양에 따라 적절한 방법을 선택해야 합니다.

#1. sys.stdin 은 ctrl+Z를 받으면 종료된다.
#그 전까지 계속 입력을 받는다.다만 개행문자 \n 까지 포함
#rstrip()또는 strip()으로 처리해서 사용한다. 
'''
arr=[]
for line in sys.stdin:
    arr.append(line.strip())
print(arr)
'''
#출력: ['1\n', '2\n', '3\n', '4\n', '5\n']
#strip적용한 출력: ['1', '2', '3', '4', '5']


#2. sys.stdin.read() 
#파일을 처음부터 끝까지 읽을때 사용됨. 반복문 없는 이유
#파일의 내용 읽어서 문자열로 가져온다.
'''
a=sys.stdin.read() 
print(a)
'''


#3.sys.stdin.readline()
#한줄 씩 읽을 때 사용, while반복문 이용,
#더 이상 읽을 줄 없을 때 빈 문자열 반환
'''
line=None
while line!="":
    line=sys.stdin.readline().strip()
    print(line)
'''
#4.sys.stdin.readlines()
#함수는 표준 입력(stdin)에서 여러 줄을 입력받고, 
#이를 각 줄을 구분하는 줄 바꿈 문자(\n)를 기준으로 분리하여 
#리스트에 저장합니다. 이 때, 입력이 종료되거나 Ctrl+Z (Windows)
# 또는 Ctrl+D (Unix/Linux) 키 조합을 입력하면 입력이 종료되고 
#readlines() 함수는 그때까지 입력된 모든 줄을 반환합니다.
#그리고 각 줄의 끝에는 줄 바꿈 문자(\n)가 포함됩니다.
lines=sys.stdin.readlines()
stripped_line=[line.strip() for line in lines] #리스트 컴프리헨션 코드 
print(stripped_line) 