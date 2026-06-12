class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')':'(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if stack and c in pair and pair[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
  
        return len(stack) == 0
# 1. Add the value to the stack
# 2. if the current char is in our map keys and the end value of 
#    the stack is the pair of that, pop from the stack 
# 3. if either is false, return False
# 4. At the end, if our stack in empty, we return True

