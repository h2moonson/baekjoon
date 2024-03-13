## 두 수가 주어졌을 때, 3가지 case중 어떤 것인지를 구하는 프로그램을 작성
while True : 
    A = int(input())
    if A == -1:
        break
    factor = [ i for i in range (1, A) if A % i == 0]
    #print(factor)
    tot = sum(factor)
    # factor_str = [str(i) for i in factor]
    # print(factor_str)
    # if tot == A: 
    #     print(A, "=", " + ".join(factor_str))
    if tot == A:
        print(A, "="," + ".join(map(str, factor)))
    else: 
        print(A, "is NOT perfect.")




    