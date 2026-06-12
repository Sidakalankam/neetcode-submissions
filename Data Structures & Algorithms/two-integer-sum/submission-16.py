class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        hashmap = {}

        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in hashmap:
                res.append(hashmap[sub])
                res.append(i)

            hashmap[nums[i]] = i
        return res
             




            
        