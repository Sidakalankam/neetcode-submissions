class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
  
        minSpeed = float('inf')
        while l <= r:
            rate = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / rate)
            
            if hours > h:
                l = rate + 1
            elif hours <= h:
                r = rate - 1
                minSpeed = min(minSpeed, rate)
        
        return minSpeed
            
                
                
