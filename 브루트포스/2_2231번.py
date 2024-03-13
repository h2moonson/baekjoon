def find_result(num):
    test=[]
    origin=num
    #print("hi1")
    while num!=0:
        #2print(num)
        b = num %10
        num//=10
        test.append(b)

    return origin + sum(test)
    # sum_number = sum(map(int, str(i))) 
    # item = i + sum_number
N = int(input())
testnum = N
candidates = []
for num in range (N):
    if find_result(testnum) == N:
        candidates.append(testnum)
    testnum -=1
if len(candidates)!=0:
    print(min(candidates))
else :
    print(0)


