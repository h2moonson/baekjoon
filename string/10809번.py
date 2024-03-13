S = input()
result = []
# for num in range(97, 123):
#     test = S.find(chr(num))
#     result.append(test)

result = [S.find(chr(num)) for num in range(97, 123)]
print(*result)