from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = defaultdict(int)
        map_t = defaultdict(int)

        if len(s) != len(t):
            return False

        for c in s:
            map_s[c] += 1
        
        for c in t:
            map_t[c] += 1
        
        return map_s == map_t
        
