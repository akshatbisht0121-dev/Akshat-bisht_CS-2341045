class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def helperfunction(root,path, tar):
            if root is None :
                return

            path.append(root.val)

            if root.left is None and root.right is None:
                if sum(path) == tar:
                    ans.append(path[:])

            helperfunction(root.left, path, tar)
            helperfunction(root.right, path, tar)
            path.pop()

        helperfunction(root, [], targetSum)
        return ans
        