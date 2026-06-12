class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for i in nums:
            if i not in count:
                count[i] = i
            
            else:
                return True

        return False




        
         