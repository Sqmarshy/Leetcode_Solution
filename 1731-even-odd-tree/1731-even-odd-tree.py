# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        bfs = [root]
        flag = 0
        while bfs:
            n = len(bfs)
            for i in range(n):
                node = bfs.pop(0)
                if (node.val % 2 == flag % 2) or (i != 0 and (node.val <= prev if flag % 2 == 0 else node.val >= prev)):
                    return False
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
                prev = node.val
            flag += 1
        return True

