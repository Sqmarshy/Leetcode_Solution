# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curr):
            if not node:
                return 0

            left = dfs(node.left, max(curr, node.val))
            right = dfs(node.right, max(curr, node.val))
            res = left + right

            return res if curr > node.val else res + 1

        return dfs(root, -float('inf'))
            
        