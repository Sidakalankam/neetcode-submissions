class Solution:
    def isValid(self, s: str) -> bool:
        """Algorithm Steps:
        1. Each element is sequentially added to the stack
        2. When a closing parenthesis is encountered, the element 
            pops the corresponding opening bracket which will always be
            at the top of the stack
        3. By the end, the stack should be completely empty if it is valid 
         """ 
        
        closeToOpen = {')':'(', '}':'{', ']':'['}

        stack = []
        
        for c in s:
            # Checks if the current element is a closing bracket
            if c in closeToOpen:
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                    # We go to the next iteration if 
                    continue
            stack.append(c)
        
        return True if len(stack) == 0 else False 