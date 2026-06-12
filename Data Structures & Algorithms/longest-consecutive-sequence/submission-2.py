from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)  # Convert to set for O(1) lookups
        longest = 0

        for num in numSet:
            # Only start counting if `num` is the beginning of a sequence
            if num - 1 not in numSet:
                length = 1
                current = num

                # Count the length of the consecutive sequence
                while current + 1 in numSet:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest



