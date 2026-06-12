class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # arr = [6,2,9,3,4,7]
        # output = [9,9,7,7,7,-1]

        # 1. traverse the array in reverse order right to left
        # 2. create an output array
        # 3. keep track of the maximum number to the right
        # 4. make last element -1
        

        max_right = -1

        res = [0] * len(arr)

        for i in range((len(arr) - 1), -1, -1):
            res[i] = max_right
            max_right = max(max_right, arr[i])

        return res







