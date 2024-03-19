import sys
N = int(sys.stdin.readline())

def top (stk):
    if len(stk)!=0:
        return stk[-1]
    else: return -1 
def size (stk):
    return len(stk)
def pop (stk): 
    if len(stk)!=0:
        return stk[-1]
    else: return -1
def is_empty(stk):
    value = len(stk)
    if value == 0: 
        return 1 
    else: return 0

    
if __name__ == "__main__":
    stack  = []
    for _ in range (N): 
        order = sys.stdin.readline().split()
        if len(order)==2: 
            if order[0]=="push":
                num = int(order[1])
                stack.append(num)
        else: 
            match order[0]:
                case "top":
                    print(top(stack))
                case "size":
                    print(size(stack))
                case "pop":
                    print(pop(stack))
                    if len(stack)!=0: stack.pop(-1)
                case "empty":
                    print(is_empty(stack))