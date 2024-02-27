class Node:
    def __init__(self,val,prev,next):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage,None,None)
        self.current = self.head

    def visit(self, url: str) -> None:
        newNode = Node(url,self.current,None)
        self.current.next = newNode
        self.current = self.current.next

    def back(self, steps: int) -> str:
        for i in range(steps):
            if not self.current.prev:
                return self.current.val
            self.current = self.current.prev
        return self.current.val

    def forward(self, steps: int) -> str:
        current = self.current
        for i in range(steps):
            if not self.current.next:
                return self.current.val
            self.current = self.current.next
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)