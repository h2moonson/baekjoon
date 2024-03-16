N = int(input())
test = []
for i in range(N): 
    word = input()
    if word not in test: 
        test.append(word)

test.sort(key=lambda x: (len(x),x))

for word in test:
    print(word)

#$$$$$$$$$$$ 집합 자료형 활용한 방법 더 빠르다 $$$$$$$$$$$$$$$$$$$
N = int(input())
words = set()

# 중복 없이 문자열 입력 받기
for _ in range(N): 
    words.add(input())

# 중복 제거한 문자열을 길이와 알파벳 순으로 정렬하여 출력
for word in sorted(words, key=lambda x: (len(x), x)):
    print(word)
