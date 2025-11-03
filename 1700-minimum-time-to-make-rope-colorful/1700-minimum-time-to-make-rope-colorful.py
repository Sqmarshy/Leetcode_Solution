class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        prev_c, prev_v = colors[0], neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == prev_c:
                res += min(prev_v, neededTime[i])
                prev_v = max(prev_v, neededTime[i])
            else:
                prev_c, prev_v = colors[i], neededTime[i]
        return res