# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        curr = root
        min_dif = float('inf')
        res = 0

        while curr:
            if target == curr.val:
                return curr.val
            curr_dif = abs(curr.val - target)
            if curr_dif < min_dif:
                res = curr.val
                min_dif = curr_dif
            if target < curr.val:
                curr = curr.left
            elif target > curr.val:
                curr = curr.right
        
        return res

        

