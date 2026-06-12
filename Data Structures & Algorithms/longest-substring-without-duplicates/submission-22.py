class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Input: string s

        Output: longest sequence of letters without repeats

        Information Needed: 
        1. We need to check if the current char was seen before in the sequence
        2. We need to keep track of the count and then reset it if we have seen the current char before
        3. We need to keep track of the max count

        How to store:
        1. We can use a hashset to store the chars in our current window
        2. If we see a repeated char, we can remove from the set

        How to process:
        1. Use a sliding window
        2. left and right pointer start at 0
        3. r keeps going as long as the window has no repeated chars and add the chars to the set
        4. if r reaches a repeated character, 
           1.. we move l by 1 until the window doesn't repeat chars and delete l from the set and we continue until r isn't in the set


        # abba


        '''

        seen = set()

        l = 0

        longest = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, r - l + 1)

        return longest
            
                
