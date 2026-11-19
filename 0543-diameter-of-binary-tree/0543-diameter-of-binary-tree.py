class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0
        def dfs(root):
            nonlocal diameter
            if not root:
                return 0

            l=dfs(root.left)
            r=dfs(root.right)
            diameter=max(diameter,r+l)

            return max(l,r)+1
        dfs(root)
        return diameter
        