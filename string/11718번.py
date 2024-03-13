test_list = []
while True:
    try:
        letter=input()
        if not letter: 
            break # 빈 줄이면 종료 
        test_list.append(letter)
    except EOFError: #임의로 터미널에서 ctrl+Z누르고 엔터치면 됨 
        break
    
for things in test_list:
    print(things)