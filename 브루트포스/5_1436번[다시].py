#영화감독 숌 , 종말의 수 666, 1666, 2666, 3666, 4666, 5666, 6666 부터 꼬이기시작 
N = int(input())
def generate_apocalytic_numbers(N):
    numbers = []
    count = 0
    num = 666
    while count < N:
        if '666' in str(num):
            numbers.append(num)
            count+=1
        num+=1
    return numbers 
result = generate_apocalytic_numbers(N)
print(result[N-1])

# if "666" in ""
# if N !=0:
#     print(str(N)+"666")
# else : 
#     print("666")
    
# #리스트 원소로넣어서 연속으로 6이 세번 나오는 경우를 카운트 해볼까? 
# #크기 비교는 비교 연산자로 수행하면 되긴함
# 1: 666
# 2: 1666
# 3: 2666
# 4: 3666
# 5: 4666
# 6: 5666
# 7: 6660
# 8: 6661
# ~
# 16: 6669
# 17: 7666
# 18: 8666