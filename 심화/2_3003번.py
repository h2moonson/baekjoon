#검정색피스는 모두 존재, 흰색 피수는 모자람 
#16개의 피스를 사용하면(킹1개, 퀸1개, 룩2, 비숍2, 나이트2, 폰8개)
# [KING, QUEEN, ROOK,BISHOP, KNIGHT, PAWN]
PIECES = list(map(int, input().split()))
#print(PIECES)
OG_PIECES = [1, 1, 2, 2, 2, 8]
LACKING_PIECES = [OG_PIECES[num]-PIECES[num] for num in range (6)]
print(*LACKING_PIECES)