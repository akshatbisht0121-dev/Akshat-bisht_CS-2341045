class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def helperFunction(root, left):
            if root is None:
                return
            if left and root.left is None and root.right is None:
                self.sum += root.val
            helperFunction(root.left, True)
            helperFunction(root.right, False)
        helperFunction(root, False)
        return self.sum