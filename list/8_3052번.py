# 두 자연수 A, B있을 때 A&B 는 A를 B로 나눈 나머지 
# 10개 받고, 42로 나눈 나머지, 서로 다른 값이 몇개인지 출력
# numpy의 unique 를 쓰면 되는데? !
remainder = []
for _ in range (10): 
    remainder.append(int(input()) % 42)
unique = []
for num in range (10):
    test = remainder[num]
    if test not in unique: 
        unique.append(test) 
print(len(unique))
    
