class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We know that the max rate of eating is the largest element in the piles array
        # And the smallest is 1 so we can run binary search on that interval
        # So we can set our left and right pointers to 1 and the max of piles respectively
        # The mid is the first k value we're checking
        # So for every k value we try, we go through the array and ceiling divide the k by the value
        # if k / piles[i] over the entire array exceeds h, we know our rate is too slow
        # so then we look at the right half of 1 - max(piles)
        # if k / piles for the entire array falls within h, we check the left half to find a possibly smaller one


        l = 1
        r = max(piles)
        minRate = float('inf')
        while l <= r:
            mid = l + (r - l) // 2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / mid)
            
            
            
            if hours > h:
                l = mid + 1
            else:
                minRate = mid
                r = mid - 1

        return minRate

                
