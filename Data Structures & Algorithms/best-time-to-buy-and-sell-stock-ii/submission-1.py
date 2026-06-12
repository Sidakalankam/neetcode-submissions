class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        maxp = 0
        l = 0
        r = 1

        while r < len(prices):
            # If profit is possible, take it
            if prices[r] > prices[l]:
                maxp += prices[r] - prices[l]
            # Move left pointer to current right
            l = r
            r += 1

        return maxp
