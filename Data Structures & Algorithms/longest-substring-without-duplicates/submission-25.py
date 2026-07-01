class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0

        longest = 0

        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            length = (r - l) + 1

            longest = max(length, longest)

            seen.add(s[r])

        return longest