class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def maxCount(count):
            max_val = 0
            max_key = None
            
            for key, val in count.items():
                if val > max_val:
                    max_val = val
                    max_key = key
            
            return max_val

        l = 0
        r = 0
        
        max_len = 0
        
        count = defaultdict(int)
        
        
        for r in range(len(s)):
            window = r - l + 1
            count[s[r]] += 1
            
            while window - maxCount(count) > k:
                count[s[l]] -= 1
                l += 1
                window = r - l + 1
            
            max_len = max(max_len, window)
                
        return max_len
		
		
			
		
		
		
		
		


        
