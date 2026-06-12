class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binSearch(nums, val):
            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = (l + r) // 2
                if val == nums[mid]:
                    return True  # Index of the found value
                elif val < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return False  # Value not found
        
        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2
            # Fix: Use matrix[mid] instead of mid when calling binSearch
            res = binSearch(matrix[mid], target)

            if res:  # If found, return True
                return True
            else:
                # Fix: Use matrix[mid][0] and matrix[mid][-1] for row bounds
                if target < matrix[mid][0]:  
                    r = mid - 1
                else:
                    l = mid + 1
        return False


                 
            
           






            
