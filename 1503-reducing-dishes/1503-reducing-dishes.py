class Solution:
    def maxSatisfaction(self, sat: List[int]) -> int:
        sat.sort()
        n = len(sat)
        memo = [[None] * (n + 1) for _ in range(n + 1)]
        def dp(idx, count):
            if idx >= len(sat):
                return 0

            if memo[idx][count - 1]:
                return memo[idx][count - 1]

            pick = dp(idx + 1, count + 1) + (count * sat[idx])
            no_pick = dp(idx + 1, count)

            res = max(pick, no_pick)
            memo[idx][count - 1] = res
            return res

        final = dp(0, 1)
        return final