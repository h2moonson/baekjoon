'''
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
'''
N=int(input())
for i in range (1,N+1):
    for  j in range (N-i): 
        print(" ",end='')
    for k in range (i):
        print('*',end='')
    print("")

#문자열 곱을 활용하는 방법 
for i in range(1,N+1):
    print(" "*(N-i)+"*"*i)