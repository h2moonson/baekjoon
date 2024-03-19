import sys
T = int(input())
lines = [sys.stdin.readline().split() for _ in range (T)]
for word in lines: 
    for i in range (len(word)):
        word[i] = word[i][::-1]
    print(*word)
