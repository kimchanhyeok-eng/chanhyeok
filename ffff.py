class Node: # 노드 클래스 구현
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class NodeMgmt: # 노드 삭제하고 추가하고 메서드 
    def __init__(self, data):   #이니셜라이져
        self.head = Node(data)
        
    def add(self, data):  # 이게 노드 추가하는거
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
        
    def desc(self): # 노드에 뭐있는지 조회해보는거
        node = self.head
        while node:
            print (node.data)
            node = node.next
    
    def delete(self, data): #노드 지우기 ㅋㅋ
        if self.head == '':
            print ("해당 값을 가진 노드가 없습니다.")
            return
        
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next

"""  # 노드 만들어보기
linkedlist1 = NodeMgmt(0)
linkedlist1.desc() """


""" # 헤드확인
linkedlist1.head """

""" # 헤드 지우기
linkedlist1.delete(0) """

""" # 여러개 노드추가
for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc() """

""" # 하나 중간꺼 삭제
linkedlist1.delete(4) """

"""  # 다시조회
linkedlist1.desc() """