from collections import Counter
from typing import List

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxNum = -1
        for key, val in count.items():  # val is the frequency
            if val == 1:
                maxNum = max(maxNum, key)
        return maxNum