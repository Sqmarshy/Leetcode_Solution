class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        memo = {}
        def dp(house, color):
            key = (house, color)
            if key in memo:
                return memo[key] 
            if house >= len(costs):
                return 0
            
            choices = [0, 1, 2]
            choices.pop(color)
            first = dp(house + 1, choices[0]) + costs[house][color]
            second = dp(house + 1, choices[1]) + costs[house][color]
            res = min(first, second)
            memo[key] = res
            return res

        res = float('inf')
        for i in range(3):
            res = min(res, dp(0, i))
            memo = {}
        return res
            