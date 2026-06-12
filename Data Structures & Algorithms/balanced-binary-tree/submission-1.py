# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def getHeight(node):
            if not node:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))

        def checkNode(node):
            if not node:
                return True

            height_left = getHeight(node.left)
            height_right = getHeight(node.right)

            if abs(height_left - height_right) > 1:
                return False

            return checkNode(node.left) and checkNode(node.right)

        return checkNode(root)
            
            
            