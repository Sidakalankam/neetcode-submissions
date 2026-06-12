# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Algorithm:
1. To reverse a Linked List, we simply have to flip the direction
   of the next pointer for every node
2. We start by saving the next node in the list before traversing
3. We then flip the pointer and have the current node as the previous one
4. we then move onto the next node
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev