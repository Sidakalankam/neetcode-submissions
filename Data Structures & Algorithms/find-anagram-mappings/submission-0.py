class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # loop through nums2 and create hashmap to map values to indexes
        # example: {50:1, 12:2. ...}
        # then loop through nums1 and find the key and store the index at that position in the output array

        res = []

        num_to_idx = defaultdict(int)

        for i, num in enumerate(nums2):
            num_to_idx[num] = i
            print(num_to_idx)

        for num in nums1:
            res.append(num_to_idx[num])


        return res

        