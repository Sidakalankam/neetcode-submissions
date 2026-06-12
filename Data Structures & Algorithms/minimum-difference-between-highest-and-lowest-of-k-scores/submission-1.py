class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # [1,2,3,3,5,6]
        # sort nums array
        # set two pointers l and r
        # set l to 0 and r to k - 1
        # have a variable called min_diff and initialize to nums[r] - nums[l]
        # in each iteration, calculate the min between the current diff and min_diff
        # at the end move l and r by 1

        nums.sort()

        l = 0
        r = k - 1
        min_diff = float("inf")
        while r < len(nums):
            curr_min = nums[r] - nums[l]
            min_diff = min(curr_min, min_diff)
            l += 1
            r += 1

        return min_diff