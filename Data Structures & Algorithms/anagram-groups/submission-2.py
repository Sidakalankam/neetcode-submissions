class Solution:

    '''
    1. create groupp hashmap
    2. for each word we build a frequency array to store the count of each letter
    3. we then make the key a tuple of the count array
    4. we can then append the groups 1 by 1

    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []

        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)

            groups[key].append(word)

        
        for group in groups.values():
            res.append(group)

        return res

    



        
