# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deepest_path = []
        def dfs(node, path):
            nonlocal deepest_path
            if not node:
                return
            path.append(node.val)
            dfs(node.left, path)
            dfs(node.right, path)

            if not deepest_path:
                deepest_path.append(path.copy())
            else:
                if len(deepest_path[-1]) < len(path):
                    deepest_path = [path.copy()]
                elif len(deepest_path[-1]) == len(path):
                    deepest_path.append(path.copy())
            path.pop()
            return
        
        dfs(root, [])
        print(deepest_path)
        depth = len(deepest_path[0])
        if len(deepest_path) == 1:
            target = deepest_path[0][-1]
        else:
            for i in range(depth - 1, -1, -1):
                found = True
                target = deepest_path[0][i]
                for j in deepest_path:
                    if j[i] != target:
                        found = False
                        break
                if found:
                    break
        res = []
        def dfs2(node):
            if not node:
                return
            if node.val == target:
                res.append(node)
                return
            dfs2(node.left)
            dfs2(node.right)
        dfs2(root)
        
        return res[0]