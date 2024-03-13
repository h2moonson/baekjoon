# 응시자수 n명중 상을 받는 사람은 k명 
N, k = map(int, input().split())
score = list( map(int, input().split()) )
score.sort()
print(score[N-k])