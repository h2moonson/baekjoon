x, y, w, h = map(int, input().split())
h -= y
w -= x
print(min(x,y,w,h))

