from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = Counter(s1)

        l = 0
        

        counter2 = defaultdict(int)

        for r in range(len(s2)):
            counter2[s2[r]] += 1
            window = r - l + 1

            if window > len(s1):
                counter2[s2[l]] -= 1
                if counter2[s2[l]] == 0:
                    del counter2[s2[l]]

                l += 1
                window = r - l + 1
            
            if counter1 == counter2:
                return True

        return False
                


            




        

         