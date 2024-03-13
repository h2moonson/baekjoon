#길이가 a,b,c 가 주어지고 

# triangle = list(map (int, input().split()))
# triangle = sorted(triangle)
# def valid_test(list) : 
#     if list[0] + triangle[1] > triangle[2]: 
#         return 1 
#     else: 
#         return -1 
# if triangle[0] + triangle[1] > triangle[2]: 
#     print(sum(triangle))
# else: 
#     while valid_test(triangle) != 1:
#         triangle[2]-=1
#     print(sum(triangle))

li = sorted(map(int, input().split()))
res = li[0] + li[1] + min(li[2], li[0]+li[1]-1) 
# 가장 긴 변의 길이는 그냥 현재 작은 두 변의 합보다 1작기만 하면됨 
print(res)