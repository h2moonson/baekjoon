#slicing
word = input() #문자열은 list와 엄연히 다른 데이터 유형. 
#string은 immutable 한 시퀀스타입이며, 리스트 관련 연산들을 수행할 수는 있지만
#리스트는 아님  
word = word[::-1]
print(word)


A, B=1234, 5678
print(A[:3:1]) # A의처음 ~3번째 인덱스 이전까지 > 123출력 
print(B[:1:-1]) # B의끝 ~ 1번째 인덱스 이전까지 = 인덱스2 > 87출력


#reverse: None반환, 따라서 다시 인자로 대입해주면 안됨 
#reversed: reversed()객체 반환 

a = [1,2,3,4,5]
test = reversed(a) #아직 reversed 객체 형태
test = list(test) #리스트로 변환 
print(test)

b = [10,11,12,13]
b.reverse() 
print(b)