from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)  # Convert to set for O(1) lookups
        longest = 0
        length = 0

        for num in nums:
            if num - 1 not in nums:
                length = 1
                curr = num

                while curr + 1 in nums:
                    curr += 1
                    length += 1
                longest = max(length, longest)
        return longest






