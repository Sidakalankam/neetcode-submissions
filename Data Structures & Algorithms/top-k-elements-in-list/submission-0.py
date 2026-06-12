from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        res = []
        for i in range(len(nums)):
                count[nums[i]] += 1
                
        while k > 0:
            max_key = max(count, key=count.get)
            res.append(max_key)
            del count[max_key]
            k -= 1
        return res
        
            


            




