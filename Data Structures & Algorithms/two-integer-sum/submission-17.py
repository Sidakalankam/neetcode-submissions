class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        res = []
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                res.append(num_to_index[complement])
                res.append(i)
            num_to_index[num] = i
        
        return res
            
             




            
        