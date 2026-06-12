class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Simple to understand but not the most optimal
        # Converts linked list to integer for both lists and adds them
        # It then converts the new number into a string and iterates through it to create a linked list

        """
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
        """
        
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next



