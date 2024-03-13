N=int(input())
sequence = list(map(int, input().split()))
A=str(min(sequence))
B=str(max(sequence))
print(A+" "+B) 

#sol2 
s=sorted(sequence)
print(s)
r=reversed(s) #iterable한 객체 반환, list로 다시한번 변환해줘야함
print(list(r))
print(s[0], s[-1])