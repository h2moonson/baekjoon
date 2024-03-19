T = int(input())
PS = [input() for _ in range (T)]
for parenthesis in PS: 
    stack = [] 
    for i in range (len(parenthesis)):
        sample = parenthesis[i]  
        if sample != ')':
            stack.append(sample)
        else: 
            #print("hi1")
            if len(stack)!=0 and stack[-1]!=")":
                stack.pop()
            else: 
                #print('hi2')
                stack.append(sample)
    #print(stack)
    if len(stack)==0:
        print("YES")
    else: print("NO")