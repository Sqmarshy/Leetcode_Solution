# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, prev, curr):
            nonlocal res

            if not prev:
                left, right = 0, 0
                if node.left:
                    dfs(node.left, 'left', curr + 1)
                if node.right:
                    dfs(node.right, "right", curr + 1)
                return

            else:
                if prev == 'right': 
                    if node.right:
                        dfs(node.right, 'right', 1)
                        
                    if node.left:
                        dfs(node.left, 'left', curr + 1)
                    else:
                        res = max(res, curr)
                        return
                    

                else:
                    if node.left:
                        dfs(node.left, 'left', 1)

                    if node.right:
                        dfs(node.right, 'right', curr + 1)
                    else:
                        res = max(curr, res)
                        return
                    
        
        dfs(root, '', 0)
        return res