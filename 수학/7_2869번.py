#달팽이는 올라가고 싶다 
# 낮에 A미터 올라감 , 밤에는 B미터 미끄러짐, 막대 높이는 V미터 

A, B, V = map(int, input().split())
step = A - B
days = (V - A + step - 1) // step + 1 #마지막날 전날까지 일수 계산하자
'''
step−1: 이 부분은 올림 계산을 위한 조정값입니다. 
V−A를 step으로 나누었을 때, 나머지가 있으면 실제로는 추가 하루가 더 필요합니다.

'''
print(days)

#풀이 2
#정상에 올라간후 미끄러지지 않기에 b를 빼준길이만큼만 오르면 됨

if (V-B) % (A-B) == 0 :
    print((V-B) // (A-B))
else :
    print(((V-B) // (A-B)) +1)