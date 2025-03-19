class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dp(level, idx):
            key = (level, idx)
            if key in memo:
                return memo[key]
            if level >= len(triangle):
                return 0
            if idx >= len(triangle[level]):
                return 0

            left = dp(level + 1, idx) + triangle[level][idx]
            right = dp(level + 1, idx + 1) + triangle[level][idx]

            res = min(left, right)
            memo[key] = res
            return res
        return dp(0, 0)
            