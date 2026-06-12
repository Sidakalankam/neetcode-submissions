class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            # [7,1,5,3,6,4]
        #        0 4 0 3 1
        #     [1,2,3,4,5]
        #      0 1 2 3 4

        if not prices:
            return 0

        maxp = 0
        l = 0
        r = 1



        while r < len(prices):
            currp = prices[r] - prices[l]
            if currp > 0:
                maxp += currp
                
            l = r
            r += 1

            
        return maxp
        
        