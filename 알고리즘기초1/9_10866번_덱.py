# push front, push back, pop front, pop back
# size, empty, front, back
# Deque, Double Ended Queue 
import sys
from collections import deque 

N = int(input())
if __name__ =="__main__":
    mydeq = deque()
    for _ in range (N): 
        order = sys.stdin.readline().split()
        #print(order)
        match order[0]: 
            case "push_back":
                mydeq.append(order[1])
                #print(mydeq)
            case "push_front":
                mydeq.appendleft(order[1])
                #print(mydeq)
            case "pop_front":
                if mydeq:
                    print(mydeq.popleft())
                else: 
                    print(-1)
            case "pop_back":
                if mydeq:
                    print(mydeq.pop())
                else: 
                    print(-1)
            case "front": 
                if mydeq:
                    print(mydeq[0])
                else: 
                    print(-1)
            case "back": 
                if mydeq:
                    print(mydeq[-1])
                else: 
                    print(-1)
            case "empty":
                if len(mydeq):
                    print(0)
                else: 
                    print(1)
            case "size":
                print(len(mydeq))
            
