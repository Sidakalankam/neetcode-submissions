class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, num in enumerate(temperatures):
            while stack and num > temperatures[stack[-1]]:
                popped = stack.pop()
                res[popped] = i - popped
            
            stack.append(i)

        
        return res
