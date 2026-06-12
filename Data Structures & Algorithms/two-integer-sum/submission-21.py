from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numset = defaultdict(int)
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numset:
                return [numset[complement], i]
            numset[nums[i]] = i

