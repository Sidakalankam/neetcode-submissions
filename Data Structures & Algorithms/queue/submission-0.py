class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

class Deque:
    def __init__(self):
        self.head = ListNode(-1)  # dummy head
        self.tail = self.head     # tail points to dummy initially
    
    def isEmpty(self) -> bool:
        return self.head.next_node is None
    
    def append(self, value: int) -> None:
        new_node = ListNode(value)
        self.tail.next_node = new_node
        self.tail = new_node
        
    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        new_node.next_node = self.head.next_node  # Fix: connect to existing list
        self.head.next_node = new_node
        
        # Fix: update tail if this is the first element
        if self.tail == self.head:
            self.tail = new_node
        
    def pop(self) -> int:
        if self.isEmpty():
            return -1
            
        # Fix: handle single element case
        if self.head.next_node == self.tail:
            val = self.tail.val
            self.head.next_node = None
            self.tail = self.head
            return val
            
        # Find second-to-last node
        curr = self.head
        while curr.next_node != self.tail:
            curr = curr.next_node
        
        val = self.tail.val
        curr.next_node = None
        self.tail = curr
        return val
    
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
            
        node_to_remove = self.head.next_node
        val = node_to_remove.val
        self.head.next_node = node_to_remove.next_node
        
        # Fix: update tail if we removed the last element
        if node_to_remove == self.tail:
            self.tail = self.head
            
        return val