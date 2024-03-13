#런타임 에러를 해결해야하는 문제 
#try except문으로 예외처리를 해주자
'''
while (True): 
    try:
        A,B=map(int,input().split())
        print(A+B)
    except: break
'''
import sys

for line in sys.stdin:
    A,B=map(int,line.split())
    print(line)
    print(A)
    print(B)
    print(A+B)

'''

split() 메서드는 기본적으로 문자열을 공백 문자 (공백, 탭, 개행 문자 등)을
기준으로 분할합니다. 따라서 split()을 사용하여 문자열을 분할하면
문자열에 있는 공백 문자와 줄 바꿈 문자(\n)는 분할된 결과에 포함되지 않습니다. 

text = "Hello World\nPython"
words = text.split()

words 리스트에는 "Hello", "World", "Python" 세 개의 문자열이
들어가며 줄 바꿈 문자(\n)는 분할 결과에 포함되지 않습니다.
'''