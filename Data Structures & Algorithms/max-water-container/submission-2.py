class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        1. have two pointers one at each end
        2. first calculate the area by taking the difference in postition aka the length and multiplying by the smaller value
        3. Then compare the current area to the max area so far and take the max.
        4. Then, whichever value is smaller, shift it inward because the length gets smaller so you want a larger value
        5. Repeat that process until l and r equal each other
        '''

        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            length = (r - l)
            area = length * min(heights[l], heights[r])

            max_area = max(area, max_area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1

        return max_area