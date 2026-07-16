class Solution:
    def isValid(self, s: str) -> bool:
        '''
        1. Define a close to open hashmap of the brackets
        2. Iterate through the string
        3. If the current element is a closing bracket, if the top of the stack is the corresponding opening bracket, pop it from the stack and continue
        4. If not, append current item to stack
        5. At the end, we can check if the stack is empty and return true if it is, or false if not
        '''

        stack = []

        closed = ')}]'

        close_to_open = {')': '(', '}':'{', ']': '[' }

        for c in s:
            if c in closed:
                if stack and close_to_open[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if len(stack) == 0 else False



        