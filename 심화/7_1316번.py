#그룹 단어 : ccazzzzbb
N = int(input())  # 입력받을 문자의 개수
count = 0
# 풀이1 : count를 0부터 시작
for _ in range(N):
    group_word = True
    word = input()

    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                group_word = False
                break

    if group_word:
        count += 1

print(count)

#풀이 2 : count를 N부터 시작해서 빼기
count = N
for _ in range (N):
    word = input()
    for j in range (0, len(word)-1):
        if word[j] == word [j+1]:
            pass
        elif word[j] in word[j+1:]:
            count -=1
            break
print(count)
