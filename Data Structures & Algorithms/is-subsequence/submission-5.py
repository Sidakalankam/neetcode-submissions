class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

    # t = popular
    # s = olar

    # 1. s should have same chars as t
    # 2. should be in same order
    
    # 1. have two pointers set to the beginning of s and t
    # 2. if s and t match, move s forward. t moves no matter what
    # 3. the loop ends when t reaches the end
    # 4. have an output string that has the same characters
    # 5. if s and the output string match then return true else false

        if not s:
            return True
        if not t:
            return False

        i = 0
        j = 0

        res = ''

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                res += s[i]
                i += 1

            j += 1

        return s == res


        
        