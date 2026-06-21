class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        seen = set(nums)
        longest = 0

        length = 1
        for num in seen:
            if num - 1 not in seen:
                length = 1
                while num + length in seen:
                    length += 1
                longest = max(length, longest)
        
        return longest
                
            

        

        '''
        When we reach the start of a sequence:
        1. Save that

        '''
