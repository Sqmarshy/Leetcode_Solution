# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        pos = defaultdict(list)
        mini, maxi = float('inf'), -float('inf')
        bfs = deque([[root, 0]])
        while bfs:
            n = len(bfs)
            for _ in range(n):
                node, position = bfs.popleft()
                pos[position].append(node.val)
                mini = min(position, mini)
                maxi = max(position, maxi)
                if node.left:
                    bfs.append([node.left, position - 1])
                if node.right:
                    bfs.append([node.right, position + 1])

        res = []
        for i in range(mini, maxi + 1):
            res.append(pos[i])
        return res
