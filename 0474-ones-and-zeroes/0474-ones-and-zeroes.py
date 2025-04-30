class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = [(s.count('0'), s.count('1')) for s in strs]
        memo = {}
        def dp(idx, x, y):
            key = (idx, x, y)
            if key in memo:
                return memo[key]
            if x < 0 or y < 0 :
                return -999999
            if idx == len(counts):
                return 0
            
            choose = dp(idx + 1, x - counts[idx][0], y - counts[idx][1]) + 1
            skip = dp(idx + 1, x, y)
            res = max(choose, skip)

            memo[key] = res
            return res

        return dp(0, m, n)