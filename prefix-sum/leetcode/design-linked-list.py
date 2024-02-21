class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        node = self.head
        for i in range(index+1):
            node = node.next
            if not node:
                return -1
        return node.val
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if not self.head.next:
            self.head.next = newNode
            self.tail = newNode
            return
        newNode.next = self.head.next
        self.head.next = newNode

    def addAtTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        node = self.head
        for i in range(index):
            node = node.next
            if not node:
                return
        if node.next is None:
            self.tail = newNode
        newNode.next = node.next
        node.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        node = self.head
        for i in range(index):
            node = node.next
            if not node:
                return
        if node.next:
            if node.next.next is None:
                self.tail = node
            node.next = node.next.next

    
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)