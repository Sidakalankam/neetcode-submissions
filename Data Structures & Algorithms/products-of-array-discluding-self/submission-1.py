class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output_array = [1]*n

        # calculate the left product
        left = 1
        for i in range(n):
            output_array[i]=left
            left = left*nums[i]
        
        # calculate the right product
        right=1
        for i in range(n-1, -1,-1):
            output_array[i]*=right
            right*=nums[i]

        return output_array