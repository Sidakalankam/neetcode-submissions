class Solution:
    """
    Algorithm:
    1. Use two pointers, left (l) and right (r), to represent the current search range.
    2. While the search range is valid (l < r):
        - Calculate the middle index (mid) of the range.
        - If the value at mid is greater than the value at r, the minimum must be in the right half.
          - Move the left pointer (l) to mid + 1.
        - Otherwise, the minimum is in the left half (including mid).
          - Move the right pointer (r) to mid.
    3. When the loop exits, l will point to the index of the minimum element.
    """
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:  # Minimum is in the right half
                l = mid + 1
            else:  # Minimum is in the left half or at mid
                r = mid

        return nums[l]  # l will point to the index of the minimum


        