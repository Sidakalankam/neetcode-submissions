class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,0,0,2,5]

        # set 2 pointers the left one at the beginning of the array and the right at the 2nd element
        # if the element at the left is 0 and right pointer and the right is nonzero swap them
        # if the element at l is nonzero, move l by 1
        # right should always move no matter what


        l = 0
        r = 1

        while r < len(nums):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
            
            if nums[l] != 0:
                l += 1

            r += 1


        