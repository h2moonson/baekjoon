# if three angles are equal : Equilateral
# if two are equal : Isosceles
# if none are the same : Scalene 
angle=[]
for i in range (3):
    angle.append(int(input()))
if sum(angle) != 180:
    print("Error")
else: 
    test = set(angle)
    #print(test)
    type = len(test)
    if type == 3 :
        print("Scalene")
    elif type == 2: 
        print("Isosceles")
    else: 
        print("Equilateral")