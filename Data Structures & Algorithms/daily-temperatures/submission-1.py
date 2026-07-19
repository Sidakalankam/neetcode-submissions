class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [40, 28]
        # [1,0,1,0,0,0]
        '''
        1. Create a stack, a num_to_idx hashmap and an output array the size of temperatures with all 0 values to start
        2. iterate through the array and while the stack is non empty and the current number is grater than the top element:
        3. We pop from the stack and take the diff of the current number's index and the popped element's index and assign it to the index in the outpu array
        4. At the end of the iteration, push the current element to the stack
        5. Finally, we return the output array
        '''

        stack = []
        res = [0] * len(temperatures)

        for i, num in enumerate(temperatures):
            while stack and num > temperatures[stack[-1]]:
                popped = stack.pop()
                res[popped] = i - popped
            
            stack.append(i)
            

        return res