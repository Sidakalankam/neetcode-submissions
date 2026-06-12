class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) * 2
        
        for i, num in enumerate(nums):
            ans[i] = num
            ans[i + len(nums)] = num

        return ans

    # [1,4,1,2]
    # [1,4,1,2,1,4,1,2]