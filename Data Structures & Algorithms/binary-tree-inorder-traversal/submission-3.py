# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # use recursion to traverse the tree
        # base case is that the node we hit does not exist
        # okay so the idea is we recursively search the left subtree
        # then we append the value of the node
        # then we apply the same to the right subtree
        # we then call the inorder function on the root node
        # finally we return the result array
        
        res = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res