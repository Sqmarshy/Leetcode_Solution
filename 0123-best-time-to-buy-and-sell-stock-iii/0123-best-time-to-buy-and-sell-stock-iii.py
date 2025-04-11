class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(idx, buy, count):
            key = (idx, buy, count)
            if key in memo:
                return memo[key]
            if idx >= len(prices):
                return 0
                
            if not buy:
                if count >= 2:
                    res = dp(idx + 1, buy, count)
                else:
                    get = dp(idx + 1, 1, count) - prices[idx]
                    skip = dp(idx + 1, buy, count)
                    res = max(get, skip)
            else:
                sell = dp(idx + 1, 0, count + 1) + prices[idx]
                skip = dp(idx + 1, buy, count)
                res = max(sell,skip)
            
            memo[key] = res
            return res
        return dp(0, 0, 0)