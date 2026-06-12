class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
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



        