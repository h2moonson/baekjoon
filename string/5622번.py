# 숫자 1= 1초 ,그보다 큰 수= 더 오래걸림 , 한칸옆일수록 1씩 초 증가
# 3의 배수 구하는 문제 
# print(ord("A")) #A = 65  B = 66, C = 67
# print(ord("Z")) #Z = 90
dial = input()
time=0
for num in dial: 
    N = ord(num)  #아스키 코드로 하지말고 for num in "ABC"이런식으로도 ok
    if N<=67: 
        time+=3
    elif N<=70:
        time+=4
    elif N<=73:
        time+=5
    elif N<=76:
        time+=6
    elif N<=79:
        time+=7
    elif N<=83:
        time+=8
    elif N<=86:
        time+=9
    else:
        time+=10
print(time)
#풀이 2
DIAL = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
S=input()
time=0
for s in S:
    for idx, element in enumerate(DIAL): 
        if s in element:
            time+=(idx+3)

alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
#풀이3 
#index() 함수는 리스트에서 주어진 값의 첫 번째 발생 위치(인덱스)를 반환합니다. 예를 들어:
#주의, 없는 경우 ValueError 발생, 예외처리 필요 
time = 0
for unit in alpabet_list :  
    for i in unit:  # alpabet 리스트에서 각 요소를 꺼내서 한글자씩 분리
        for x in word :  # 입력받은 문자를 하나씩 분리
            if i == x :  # 두 알파벳이 같으면
                time += alpabet_list.index(unit) +3  # time = time + index +3
print(time)