# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0
        def dfs_inner(node, track):
            if not node:
                return 0

            left = dfs_inner(node.left, track + node.val)
            right = dfs_inner(node.right, track + node.val)
            to_add = 0
            if track + node.val == targetSum:
                to_add = 1
            
            track -= node.val
            return left + right + to_add

            
        def dfs_outer(node):
            if not node:
                return 0

            result = dfs_inner(node, 0)
            
            left = dfs_outer(node.left)
            right = dfs_outer(node.right)

            return left + right + result

        return dfs_outer(root)