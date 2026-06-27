class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        1. We start with two pointers one at the beginning and one at index 1
        2. We then loop through until the right pointer reaches the end. 
        3. We then calculate the profit and if it's negative, we move our left pointer to match the right pointer's position
        4. We then compare the profit to the max so far. 
        5. The right pointer moves no matter what
        '''

        l = 0

        largest = 0

        for r in range(len(prices)):
            profit = prices[r] - prices[l]

            largest = max(profit, largest)

            if profit < 0:
                l = r

        return largest