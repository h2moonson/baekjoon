#  /M*100, M 
# N개의 과목, max 점수 = M 
N = int (input())
score =list(map(int, input().split()))
M=max(score)
tot=0
for i in range (N):
    score[i] = score[i]/ M *100
    tot  += score[i]
print(tot/N)