my_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(my_list[::-1])
print(my_list[::-2])
print(my_list[::-3])

[8, 7, 6, 5, 4, 3, 2, 1] #처음부터 끝까지 -1단위로 슬라이싱 
                         #= 뒤집어진 리스트 전체 복사와 같다 
[8, 6, 4, 2]
[8, 5, 2]