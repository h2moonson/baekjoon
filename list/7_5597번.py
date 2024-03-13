# 30명 1~30번  > 28명 제출, 제출안한 두명 출석번호? 
# 1~30리스트 만들고 같은 원소있으면 pop?
''' 
attendance_book = []
attendance_book.append(int(input().split("\n")))

attendance_book = sorted(attendance_book) #순차 정렬 
print(attendance_book)

for num in range (30):
    for i in range (28): 
        if num not in attendance_book[num]: 
            print(attendance_book[num]) #이런경우는 min, max 순이 아닐것 
'''

num = [i for i in range (1, 31)]

for _ in range (28): 
    data = int(input())
    num.remove(data)

print(min(num))
print(max(num))

        

