class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # abc
        # 012
        # xyz
        # 012
        # check abc
        # idx: 0
        # check xyz
        # idx: 0
        #
        # output: a

        res = ''

        greater = word2

        if len(word1) > len(word2):
            greater = word1
        
        for i in range(len(greater)):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
        return res

        
        