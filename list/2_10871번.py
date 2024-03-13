N, X = map(int, input().split())
sequence = list(map(int, input().split()))
smaller_ones = ""

for num in sequence:
    if X > num:  
        smaller_ones += str(num) + " "

print(smaller_ones)

result=[str(num) for num in sequence if num<X]
result2=['test' for num in sequence if num<X]
print(result)#['1', '4', '2', '3']
print(result2)#['test', 'test', 'test', 'test']

print(" ".join(result)) #문자열 결합하는데 사용, iterable 객체의 각 요소를 공백 문자로 구분하여 하나의 문자열로 만듭니다.
