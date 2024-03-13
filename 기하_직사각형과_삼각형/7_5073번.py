# if three angles are equal : Equilateral
# if two are equal : Isosceles
# if none are the same : Scalene 
while True: 
    A, B, C = map(int, input().split())
    if A == B == C == 0: 
        break 
    triangle = [A,B,C]
    type = len(set(triangle))
    longest = max(triangle) #굳이 이렇게 안해도 sorted 로 정렬하고 
    # 인덱스 비교해도 됨 
    triangle.pop(triangle.index(longest))
    
    if sum(triangle) > longest: 
        if type == 3 :
            print("Scalene")
        elif type == 2: 
            print("Isosceles")
        else: 
            print("Equilateral")
    else: 
        print("Invalid")

