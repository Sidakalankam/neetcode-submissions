class Solution:
    """
Algorithm Steps:
1. Set 3 pointers: left, right and middle
2. If the target it the middle, we return the index of middle
        - if the target is less than the middle, we eliminate 
            the right half
        - if it is greater, we eliminate the right half
3. Repeat step 2 iteratively and return -1 if the target is not
    found
"""
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
        return -1
            