class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def searchArr(nums, target):
            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2

                if target == nums[mid]:
                    return True
                elif target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                
            return False

        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid = l + (r - l) // 2
            
            if searchArr(matrix[mid], target) == True:
                return True
            
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                r = mid - 1
        
        return False






