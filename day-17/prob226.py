class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        left = root.left
        right= root.right    
        root.right = self.invertTree(left)
        root.left = self.invertTree(right)
        return root