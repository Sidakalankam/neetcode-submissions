# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def reverse(head):
            curr = head
            prev = None

            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode

            return prev

        r_head = reverse(head)
        curr = r_head
        dummy = ListNode()
        prev = dummy
        dummy.next = r_head
        while curr:
            nextNode = curr.next
            if n == 1:
                prev.next = nextNode
                curr.next = None
                break
            prev = curr
            curr = nextNode
            n -= 1

        return reverse(dummy.next)
                



            






