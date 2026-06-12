# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        def dfs(node, res):
            if not node:
                res.append(None)
                return None
            
            dfs(node.left, res)
            dfs(node.right, res)

            
            res.append(node.val)
            return res
        stack1 = []
        stack2 = []

        stack1 = dfs(p, stack1)
        stack2 = dfs(q, stack2)

        return stack1 == stack2

        


            



        