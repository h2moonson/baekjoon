#1/1 
#1/2, 2/1 #분모 -1, 분자 +1
#3/1 2/2 1/3  #분자 -1 분모 +1 
#1/4 2/3 3/2 4/1 

 

#X가 주어졌을 때 X번째 분수를 구하는 프로그램
num = int(input())
line = 1
while num > line:
    num -= line 
    line += 1 

# n 번째 line에는 n개의 원소가 있음 
# 지그 재그 방향탓에 짝수 홀수 케이스로 나눠야 함 
    
# 짝수번째 line일 경우 
if line % 2 == 0:
    a = num 
    b = line - num + 1 
# 홀수번째 line일 경우 
else:  
    a = line - num + 1 
    b = num
print(f"{a}/{b}")