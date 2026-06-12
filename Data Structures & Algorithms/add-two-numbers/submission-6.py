class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Convert linked list to integer
        def linkedListToNumber(node):
            num = 0
            place = 1
            while node:
                num += node.val * place
                place *= 10  # Use integer multiplication for power of 10
                node = node.next
            return num

        # Convert integer to linked list
        def numberToLinkedList(num):
            dummy = ListNode()
            curr = dummy
            if num == 0:  # Handle case where sum is 0
                return ListNode(0)
            while num > 0:
                curr.next = ListNode(num % 10)  # Extract last digit
                curr = curr.next
                num //= 10  # Remove the last digit
            return dummy.next

        # Convert both linked lists to numbers
        num1 = linkedListToNumber(l1)
        num2 = linkedListToNumber(l2)

        # Add the numbers and convert back to a linked list
        total = num1 + num2
        return numberToLinkedList(total)
