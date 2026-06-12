class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        # {1,2,3}

        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False


        