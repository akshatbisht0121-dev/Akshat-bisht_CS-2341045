class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.tar = targetSum
        def helperFunction(root, temp):
            if root is None:
                return False
            temp += root.val
            if root.left is None and root.right is None:
                return temp == self.tar
            return helperFunction(root.left,temp) or helperFunction(root.right,temp)
        return helperFunction(root,0)  