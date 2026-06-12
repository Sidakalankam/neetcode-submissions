class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        # Connect them
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
       return self.head.next == self.tail


    def append(self, value: int) -> None:
        new_node = ListNode(value)
        prev_node = self.tail.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = self.tail
        self.tail.prev = new_node


    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        next_node = self.head.next
        next_node.prev = new_node
        new_node.next = next_node
        new_node.prev = self.head
        self.head.next = new_node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        lastNode = self.tail.prev
        secondLastNode = lastNode.prev
        secondLastNode.next = self.tail
        self.tail.prev = secondLastNode

        lastNode.next = None
        lastNode.prev = None

        return lastNode.val


    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        firstNode = self.head.next
        secondNode = firstNode.next

        secondNode.prev = self.head
        self.head.next = secondNode

        firstNode.next = None
        firstNode.prev = None

        return firstNode.val




# -1 <-> 20 -> 10 <- -1
#  h                  t
        
