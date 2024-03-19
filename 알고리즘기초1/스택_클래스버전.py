import sys
class Stack: 
    def __init__(self):
        self.stack = []

    def top(self): 
        if self.is_empty():
            return -1
        return self.stack[-1]
        
    def size(self): 
        return len(self.stack)
    
    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack)==0

if __name__ == "__main__":
    N  = int(sys.stdin.readline())
    stack = Stack()

    for _ in range (N):
        order = sys.stdin.readline().split()
        match order[0]:
            case "push":
                num = int(order[1])
                stack.stack.append(num)
            case "top":
                print(stack.top())
            case "size":
                print(stack.size())
            case "pop":
                print(stack.pop())
            case "empty":
                if stack.is_empty():
                    print(1)
                else: print(0)        