class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        currMax = 0
        while l < r:
            height = min(heights[l], heights[r])
            base = r - l
            area = base * height
            currMax = max(currMax, area)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return currMax
        