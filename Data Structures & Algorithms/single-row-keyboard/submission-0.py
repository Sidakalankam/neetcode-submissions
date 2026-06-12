class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        # create hashmap to map val to idx in keyboard
        # loop through word
        # have a variable called total that is set to 0

        # at every letter, we can subtract the current position from the previous
        # then, we can add that difference to the total

        char_to_idx = {}

        total = 0
        prev = 0

        for i, char in enumerate(keyboard):
            char_to_idx[char] = i

        for char in word:
            total += abs(char_to_idx[char] - prev)
            prev = char_to_idx[char]

        
        return total


        