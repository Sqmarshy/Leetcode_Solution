class Solution:
    def recoverFromPreorder(self, s: str) -> Optional[TreeNode]:
        count, val = [0], []
        num, curr = [], 0
        for i in range(len(s)):
            if s[i] != '-':
                num.append(s[i])
                if curr:
                    count.append(curr)
                    curr = 0
            else:
                curr += 1
                if num:
                    val.append(int(''.join(num)))
                    num = []
        val.append(int(''.join(num)))

        n = len(count)
        idx = 0
        res = TreeNode()

        def dfs(node, level):
            nonlocal idx
            # Value
            node.val = val[idx]

            # Stop at end of input
            if idx + 1 >= n:
                return

            # Handling left
            if count[idx + 1] == level + 1:
                idx += 1
                node.left = TreeNode()
                dfs(node.left, level + 1)

            # Handling right
            if idx + 1 < n and count[idx + 1] == level + 1:
                idx += 1
                node.right = TreeNode()
                dfs(node.right, level + 1)

        dfs(res, 0)
        return res