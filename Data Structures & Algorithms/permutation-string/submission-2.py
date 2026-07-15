class Solution:
    from collections import Counter, defaultdict
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        l = 0
        s1_count = Counter(s1)
        s2_count = defaultdict(int)

        for r in range(len(s2)):
            s2_count[s2[r]] += 1
            window = r - l + 1

            if window > len(s1):
                s2_count[s2[l]] -= 1
                if s2_count[s2[l]] == 0:
                    del s2_count[s2[l]]
                
                l += 1
                
            
            if s1_count == s2_count:
                return True
        
        return False
