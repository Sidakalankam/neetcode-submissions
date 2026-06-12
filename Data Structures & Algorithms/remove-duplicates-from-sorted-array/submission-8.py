class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        if len(nums) == 1:
            return 1     
        for i in range(len(nums) - 1, 0, -1 ):
            if nums[i] == nums[i - 1]:
                nums.pop(i)

        return len(nums)
        '''

        if not nums:
            return 0

        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l