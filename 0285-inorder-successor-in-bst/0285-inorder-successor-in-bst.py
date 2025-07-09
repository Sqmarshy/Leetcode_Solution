class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        stack = []
        def dfs(node):
            if not node:
                return

            # Left Neighbour
            left = dfs(node.left)
            if left: return left

            # Node itself
            if stack and stack[-1] == p.val:
                return node
            else:
                stack.append(node.val)

            # Right Neighbour
            right = dfs(node.right)
            if right: return right
        
        res = dfs(root)
        return res
