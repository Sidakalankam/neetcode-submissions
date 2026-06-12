# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        idx = 0
        sum1 = 0
        curr = l1

        while curr:
            sum1 += curr.val * math.pow(10, idx)
            idx += 1
            curr = curr.next
            sum1 = int(sum1)

        idx = 0
        sum2 = 0
        curr = l2
        
        while curr:
            sum2 += curr.val * math.pow(10, idx)
            idx += 1
            curr = curr.next
            sum2 = int(sum2)

        finSum = str(sum1 + sum2)[::-1]

        dummy = ListNode()
        curr = dummy

        for digit in finSum:
            curr.next = ListNode(int(digit))
            curr = curr.next
        
        return dummy.next
        
        


        

        
        