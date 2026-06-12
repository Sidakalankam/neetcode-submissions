class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # one pointer starting at first char initialized to 0
        # if char is space, set/reset curLen to 0
        # if char is alpha, add 1 to the length
        # two vars for curLen and lastlen
        # at the end make sure the last word length is preserved
     

        # Edge case: "  se  "

        lastLen = 0
        curLen = 0
        
        for i in range(len(s)):
            if s[i] != ' ':
                curLen += 1
            else:
                if curLen > 0:
                    lastLen = curLen
                curLen = 0

        if curLen > 0:
            lastLen = curLen

        return lastLen

        # lastLen = [5, 2, 5, ]
                



        
        