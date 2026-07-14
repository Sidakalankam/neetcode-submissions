class Solution:
    from collections import defaultdict
    def characterReplacement(self, s: str, k: int) -> int:
        def largestCount(count):
            max_val = 0
            
            for key, val in count.items():
                if val > max_val:
                    max_val = val
                      
            return max_val

        
        l = 0
        max_length = 0

        count = defaultdict(int)

        for r in range(len(s)):
            window = r - l + 1

            count[s[r]] += 1

            while window - largestCount(count) > k:
                count[s[l]] -= 1
                l += 1
                window = r - l + 1
            
            max_length = max(max_length, window)

        
        return max_length

                