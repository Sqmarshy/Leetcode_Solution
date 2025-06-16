class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        res = []
        def dfs(node):
            if not node:
                return 0 
            
            left = dfs(node.left)
            right = dfs(node.right)

            subtree = left + right + node.val
            res.append(subtree)
            return subtree

        dfs(root)
        for i in range(len(res) - 1):
            if res[i] == res[-1] / 2:
                return True
        return False