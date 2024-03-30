import sys
if __name__ == "__main__":
    N = int(input())
    queue = []
    for _ in range (N):
        order = sys.stdin.readline().split()
        match order[0]:
            case "push":
                queue.append(int(order[1]))
            case "front":
                if len(queue)!= 0:  
                    print(queue[0])
                else: 
                    print(-1)
            case "pop":
                if len(queue)!= 0: 
                    num = queue.pop(0)
                    print(num)
                else: 
                    print(-1)
            case "back":
                if len(queue)!= 0: 
                    num = queue.pop()
                    print(num)
                    queue.append(num)
                else: 
                    print(-1)
            case "size":
                print(len(queue))
                #print(queue)
            case "empty":
                if queue: print(0)
                else: print(1)
            

