class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l = 0
        r = 1
        res = True

        while r < len(nums):
            if nums[l] % 2 != nums[r] % 2:
                l += 1
                r += 1
            else:
                return False

        return res