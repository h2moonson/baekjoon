a, b, c, d, e, f = map(int, (input().split()))
print((c*e-b*f)//(a*e-b*d), (a*f-d*c)//(a*e-b*d))

# #모든 경우의 수 ( 브루트 포스 )
# for i in range(-999,1000):
#     for j in range(-999,1000):
#         if (a*j) + (b*j) == c and (d*i) + (e*j) == f:
#             print(i,j)