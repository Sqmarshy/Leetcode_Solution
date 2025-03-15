# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dfs(node, robbed):
            key = (node, robbed)
            if key in memo:
                return memo[key]

            if not node:
                return 0

            if robbed:
                l = dfs(node.left, 0)
                r = dfs(node.right, 0)
                res = l + r
            else:
                rob = dfs(node.left, 1) + dfs(node.right, 1) + node.val
                skip = dfs(node.left, 0) + dfs(node.right, 0)
                res = max(rob, skip)
            memo[key] = res
            return res
        
        return dfs(root, 0)