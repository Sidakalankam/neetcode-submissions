class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set two pointers l and r and mid
        # set l to 0 and r to the end and mid to the middle of the array or l + r // 2
        # if the target is less than mid, move r to mid
        # if the target is greater than mid, move l to mid
        # if target is mid, return mid

        l = 0
        r = len(nums) - 1


        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1

        return -1