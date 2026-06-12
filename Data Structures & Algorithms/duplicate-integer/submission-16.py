class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe_set = set(nums)

        if len(dupe_set) != len(nums):
            return True
        else:
            return False
        