class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        idx = 0
        sum1 = 0
        curr = l1

        # Convert l1 to an integer
        while curr:
            sum1 += curr.val * math.pow(10, idx)
            idx += 1
            curr = curr.next
            sum1 = int(sum1)

        idx = 0
        sum2 = 0
        curr = l2

        # Convert l2 to an integer
        while curr:
            sum2 += curr.val * math.pow(10, idx)
            idx += 1
            curr = curr.next
            sum2 = int(sum2)

        # Calculate the final sum and convert it to a string
        finSum = str(sum1 + sum2)[::-1]

        # Build the resulting linked list
        dummy = ListNode()  # Dummy node
        current = dummy

        for i in range(len(finSum)):
            # Create a new node for each digit
            newNode = ListNode(int(finSum[i]))
            current.next = newNode
            current = current.next

        return dummy.next  # Return the head of the new linked list

        
        


        

        
        