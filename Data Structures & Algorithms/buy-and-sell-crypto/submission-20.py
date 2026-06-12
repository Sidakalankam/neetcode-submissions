class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        currProfit = 0
        profit = 0
        
        while r < len(prices):
            currProfit = prices[r] - prices[l]
            if currProfit < 0:
                l = r
            profit = max(currProfit, profit)
            print(currProfit)
            r += 1

        return profit


            

        