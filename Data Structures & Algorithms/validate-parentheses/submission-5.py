class Solution:
    def isValid(self, s: str) -> bool:

        closeToOpen = {')':'(', '}':'{', ']':'['}
        stack = []
        
        for c in s:
            if c in closeToOpen.keys():
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                    continue
            stack.append(c)
        
        return True if len(stack) == 0 else False 
        