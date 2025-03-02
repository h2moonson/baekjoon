# 백준 17413 단어 뒤집기


#1. 공백 단위로 끊는다 S = [baekjoon, online, judge]
  # 만약에 slicing이 되지 않는 경우는 공백이 없는 경우다.
  # 이때는 꺽쇄를 기준으로 < >를 체크해서 더해준다.
#2. 각 요소별로 반복문을 돌면서 뒤집고 리스트에 넣는다.
  # 이때 꺽쇄가 있다면 순방향으로 더해준다.
#3. 리스트 인자들 끼리 더할 때 다시 공백 문자를 추가해서 더한다


# 1. 구분이 되는 경우가 어떤 경우인가? < > 안과 밖, 띄어쓰기를 받는 경우
# 2. 언제 업데이트를 시킬 것인가? < 를 만났을 때, < > 밖에서 " "를 만났을 때
S = input("type what you want: ")
result = []
temp = []a
in_tag = False

for char in S:
    if char == "<":  # 태그 시작
        if temp:
            # 태그 시작 전 단어가 있는 경우 뒤집어서 추가
            temp.reverse()
            result.extend(temp)
            temp = []
        in_tag = True
        temp.append(char)
    elif char == ">":  # 태그 끝
        temp.append(char)
        result.extend(temp)  # 태그를 그대로 추가
        temp = []
        in_tag = False
    elif not in_tag and char == " ": # 태그 안이 아니고 공백문자를 받았을 경우는 뒤집어서 더하고 공백문자도 추가
        temp.reverse()
        result.extend(temp)
        result.append(char)
        temp = []
    else:
        temp.append(char)

# 마지막 단어가 남아있을 경우 처리
if temp:
    if in_tag:
        result.extend(temp)  # 태그 내용 그대로 추가
    else:
        temp.reverse()
        result.extend(temp)  # 단어를 뒤집어서 추가

# 결과 출력
print("".join(result))
