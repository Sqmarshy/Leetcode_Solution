class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deepest_path = []
        def dfs(node, path):
            nonlocal deepest_path
            if not node:
                return
            path.append(node)
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
        depth = len(deepest_path[0])
        if len(deepest_path) == 1:
            return deepest_path[0][-1]
        else:
            for i in range(depth - 1, -1, -1):
                found = True
                res = deepest_path[0][i]
                for path in deepest_path:
                    if path[i] != res:
                        found = False
                        break
                if found:
                    return res