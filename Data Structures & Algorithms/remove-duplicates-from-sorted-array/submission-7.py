class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        for i in range(len(nums) - 1, 0, -1):  # Stop at 1, not -1
            if nums[i] == nums[i - 1]:
                nums.pop(i)
        
        return len(nums)
