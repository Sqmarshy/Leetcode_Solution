# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        s1, s2 = [], []
        def dfs(node, to_add):
            if not node:
                return
            
            if not node.left and not node.right:
                to_add.append(node.val)
                return
            
            dfs(node.left, to_add)
            dfs(node.right, to_add)
            return
        
        dfs(root1, s1)
        dfs(root2, s2)

        return s1 == s2
