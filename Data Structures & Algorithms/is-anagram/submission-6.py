from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shash = defaultdict(int)
        thash = defaultdict(int)

        for c in s:
            shash[c] += 1
        
        for c in t:
            thash[c] += 1
        
        return thash == shash
        