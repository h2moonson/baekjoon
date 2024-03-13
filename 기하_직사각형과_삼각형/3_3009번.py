# x, y, w, h = map(int, input().split())
# h -= y
# w -= x
# print(min(x,y,w,h))

# 3번 
#coord = [list(map(int, input().split())) for _ in range (3)]
X = []
Y = []

for i in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in range(3):
    if X.count(X[i]) == 1:
        x = X[i]
    if Y.count(Y[i]) == 1:
        y = Y[i]

print(x, y)
