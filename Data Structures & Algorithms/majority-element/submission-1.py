class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
            
                
        for c in count:
            if count[c] > len(nums)/2:
                return c