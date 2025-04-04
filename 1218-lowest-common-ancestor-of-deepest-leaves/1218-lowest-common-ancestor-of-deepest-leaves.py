class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deepest_paths = []
        def dfs(node, path):
            # Base Cases
            if not node:
                return

            # Add current node to path and explore left right
            path.append(node)
            dfs(node.left, path)
            dfs(node.right, path)

            # See if current path length is creater than ones in deepest_path
            # Replace if current path is longer, append if equal, ignore if shorter
            if not deepest_paths:
                deepest_paths.append(path.copy())
            else:
                if len(deepest_paths[-1]) < len(path):
                    deepest_paths.clear()
                    deepest_paths.append(path.copy())
                elif len(deepest_paths[-1]) == len(path):
                    deepest_paths.append(path.copy())
            path.pop()
            return
        
        # Construct deepest_path and find the first common node
        # across all paths in reverse order
        dfs(root, [])
        
        if len(deepest_paths) == 1:
            return deepest_paths[0][-1]
        
        path_length = len(deepest_paths[0])
        for i in range(path_length - 1, -1, -1):
            res = deepest_paths[0][i]
            if all(path[i] == res for path in deepest_paths):
                return res