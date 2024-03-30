#고려해야 할 점 
#커서 가리키는 포인터 변수가 out of index 가 뜬다거나 
#삽입, 삭제 후 Llink, Rlink연결 과정에서 엉뚱한 주소값을 가리켜서 이상한 값이 들어감 
import sys 
class DNode:
    def __init__(self,data):
        self.data = data
        self.Llink = None
        self.Rlink = None 
    def setLlink(self, LLink): self.Llink = LLink
    def setRlink(self, Rlink): self.Rlink = Rlink

class DLinkedList:    
    def __init__(self): 
        self.__head = None
        self.__tail = None
        self.count = 0 # 노드의 총 개수 

    def addRear(self, num):
        nNode = DNode(num) 
        if self.__head == None: # 맨 처음 추가한다면 
            self.__head = nNode 
            self.__tail = nNode 
        else:
            self.__tail.setRlink(nNode) #기존 tail의 Rlink연결 
            nNode.setLlink(self.__tail) # 새로 추가된 원소의 Llink 연결 
            self.__tail = nNode #tail 업데이트 

        self.count += 1 

    def move_left(self): # 왼쪽으로 한칸 옮기고 tail을 수정하자 
        if self.__tail.Llink != None: # 앞으로 갈 자리가 있으면 
            self.__tail = self.__tail.Llink 
        else:
            pass

    def move_right(self):
        if self.__tail.Rlink != None: # 우측으로 갈 자리가 있으면 
            self.__tail = self.__tail.Rlink 
        else: 
            pass 
        
    def insert(self, p): 
        nNode = DNode(p)
        prev_Rlink = self.__tail.Rlink
        self.__tail.setRlink(nNode)
        prev_Rlink.setLlink(nNode) 
        nNode.setRlink(prev_Rlink)
        self.__tail = nNode 

    def delete(self):
        if self.__tail == None:  # 문장 맨 앞이면 걍 리턴때림 
            return 0
        if self.__tail.Llink == None: 
            print("맨 앞 원소 삭제함")
            new_first = self.__tail.Rlink
            new_first.setLlink(None) 
            self.__tail = None 
        else: 
            prev_front = self.__tail.Llink
            prev_front.setRlink(self.__tail.Rlink) # 삭제할 원소의 Rlink를 그 앞원소 R링크와 연결
            self.__tail.setLlink(prev_front) 
            self.__tail = prev_front #커서 위치 업뎃

    def print_list(self):
        current = self.__head
        while current:
            print(current.data, end=" ")
            current = current.Rlink
        print()


if __name__ == "__main__": 
    result = DLinkedList()
    text = sys.stdin.readline()
    n = len(text) 

    test = DLinkedList() 
    for i in range(n):
        test.addRear(text[i])
        
    M = int(sys.stdin.readline())
    for i in range(M):  
        command = sys.stdin.readline().split()
        match command[0]: 
            case "P":
                print("$삽입")
                test.addRear(command[1])
            case "L":
                print ("맨 위칸으로 ")
                test.move_left
            case "B":
                print("한칸 삭제")
                test.delete()
            case "d":
                print("오른쪽 한칸 옮김")
                test.move_right()

    test.print_list()  # 연결 리스트 출력
