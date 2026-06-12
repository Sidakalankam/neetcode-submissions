class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Helper to convert linked list to number
        def linkedListToNumber(head):
            res = 0
            place = 1
            curr = head
            while curr:
                res += curr.val * place
                place *= 10
                curr = curr.next
            return res

        # Convert both linked lists to numbers
        sum1 = linkedListToNumber(l1)
        sum2 = linkedListToNumber(l2)

        # Add the numbers and reverse the result
        finSum = str(sum1 + sum2)[::-1]

        # Build the resulting linked list
        dummy = ListNode()
        curr = dummy
        for digit in finSum:
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next
