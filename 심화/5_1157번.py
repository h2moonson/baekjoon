# #대소문자 단어주어지면, 이 단어에서 가장 많이 사용된 알파벳?
# word = input().upper() #일단 다 대문자로
# char_count = {} #딕셔너리
# for char in word:
#     # if char.isalpha(): # 알파벳인 경우만 
#     if char in char_count:
#         char_count[char]+=1
#     else:
#         char_count[char]=1
# max_count= max(char_count.values())
#                     # 반복문으로 딕셔너리의 char, count 를 뽑아서 max_count와 같다면 char를 리스트에 추가
# most_common_chars = [char for char, count in char_count.items() if count == max_count] #리스트 컴프리헨션 
# if len(most_common_chars) ==1:
#     print(most_common_chars[0])
# else: 
#     print("?")

        
# #풀이 2 
# word2 = input().upper() #일단 다 대문자로
# word_list= list(set(word)) #unipt한 애들만 집합으로 묶고 리스트로 변호나
# cnt_list = []
# for word in word_list:
#     cnt = word2.count(word)
#     cnt_list.append(cnt)
# max_num = max(cnt_list)
# if cnt_list.count(max_num)>=2: #max_num이 2개 이상일때 예외처리
#     print("?")
# else:
#     print(word_list[cnt_list.index(max(cnt))])

#풀이 3
# WORD = input().upper()
WORD ="MISSISSIP"
max_count = 0
most_common_char = []

for char in set(WORD):
    count = WORD.count(char)
    print(set(WORD))
    if count>max_count:
        max_count= count
        most_common_char= [char]
    elif count == max_count: #같을 경우에 
        most_common_char.append(char)
if len(most_common_char)==1:
    print(most_common_char[0])
else:
    print("?")