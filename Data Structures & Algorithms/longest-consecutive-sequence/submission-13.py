class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numset = set(nums)
        res = 0

        for num in numset:           # iterate set to avoid duplicate work
            if num - 1 not in numset:  # only start at sequence beginnings
                curmax = 1
                temp = num
                while temp + 1 in numset:
                    curmax += 1
                    temp += 1
                res = max(res, curmax)

        return res
