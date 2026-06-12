class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Algorithm Steps:
        1. We start by checking if the current element is a number
            and if it is, we push it to the stack
        2. If we encounter an operator, we pop the last 2 elements in the
            stack and push the result of the operation of those 2 numbers
            onto the stack
        3. At the end, we should have a single remaining element
        """
        stack = []

        for e in tokens:
            if e.isdigit() or (e.startswith('-') and e[1:].isdigit()):
                # If the element is a number, push it onto the stack
                stack.append(int(e))
            else:
                # For operators, pop the last two numbers from the stack
                b = stack.pop()
                a = stack.pop()
                if e == '+':
                    stack.append(a + b)
                elif e == '-':
                    stack.append(a - b)
                elif e == '*':
                    stack.append(a * b)
                elif e == '/':
                    # Perform integer division, truncating toward zero
                    stack.append(int(a / b))
        
        # The result is the single remaining element in the stack
        return stack.pop()



        