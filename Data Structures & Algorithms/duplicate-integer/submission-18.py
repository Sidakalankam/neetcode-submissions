class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dupe_set = set()

        for num in nums:
            if num not in dupe_set:
                dupe_set.add(num)
            else:
                return True
        return False
        