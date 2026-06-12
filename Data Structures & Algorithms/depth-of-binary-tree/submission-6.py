class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        if not root:
            return 0
        
        # Recursively calculate the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # The maximum depth is the larger of the two, plus 1 for the current node
        return max(left_depth, right_depth) + 1
        """
        if not root:
            return 0
        max_depth = 1

        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        return max_depth
            
            



