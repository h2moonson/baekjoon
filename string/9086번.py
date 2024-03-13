num = int(input())
output = []
for i in range (num):
    string = input() 
    result = (string[0]+string[-1])
    output.append(result)
for i in range (num):
    print(output[i])

#리스트 컴프리헨션 사용 >
output = [input()[0] + input()[-1] for _ in range(num)]
for result in output:
    print(result)
