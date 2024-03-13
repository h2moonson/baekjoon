# c=, c-, dz=, d-, lj, nj, s=, z=
# ljes=njak은 6개로 인식
# 없는 알파벳은 한 글자식 센다
ref_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
crotian = input()
count=0
# while (-1):
#     print("neverending")
# wrong usage of strip()  > .com을 제거한다던가 시작, 끝점의 공백을 제거한다던가를 목적

 #3줄이면 끝나는 것을 ...
for ref in ref_list:
    crotian = crotian.replace(ref," ") #c=c=의 경우 문제가 발생한다
print(len(crotian))

for ref in ref_list:
    prev = len(crotian.replace(" ",""))
    while crotian.find(ref)!= -1: #없기 전까지
        # crotian =crotian.strip(ref) 복사본을 반환하기에 원본에 다시 update
        crotian = crotian.replace(ref," ") #c=c=의 경우 문제가 발생한다
        current = len(crotian.replace(" ","")) #복사본으로 변경된 길이 확인, 원본을 변경 하지는 않음
        count += (prev-current)//len(ref)
        print(f"ref중인 애는 {ref}, 삭제한 개수는 {count }")
    # crotian  = crotian.replace(" ","")

crotian = crotian.replace(" ","") #공백으로 바꿨던 것들 지우기
leftover = len(crotian)
# print("이외의 알파벳 ", leftover)
print(count+leftover)