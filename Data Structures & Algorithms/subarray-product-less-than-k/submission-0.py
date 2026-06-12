class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # use a sliding window approach
        # set two pointers l and r to 0
        # set a product variable to 1 and result variable to 0
        # we first get the product by multiplying by the right value
        # then if the current window isn't valid due to either the product being too big or the left pointer crossing the right, we update the product and move the left pointer by 1
        # we then calculate how many subarrays are valid in the current window by taking the length of the current window and adding that to the result
        # then we return the result

        l = 0
        r = 0
        prod = 1
        res = 0

        while r < len(nums):
            prod *= nums[r]
            while l <= r and prod >= k:
                prod //= nums[l]
                l += 1
            res += (r - l + 1)
            r += 1
        
        return res
                
                

        

        

            