class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10 ** 9 + 7
        memo = {}
        def dp(state, count):
            key = (state, count)
            if key in memo:
                return memo[key]
            if state == 0 and (count == n or count == n - 1):
                return 1
            if state == 0 and count == n - 2:
                return 2
            if (state == 1 or state == 2) and count == n - 1:
                return 1

            if state == 0:
                res = dp(state, count + 1) + dp(1, count + 2) + dp(2, count + 2) + dp(0, count + 2)
            elif state == 1:
                res =  dp(2, count + 1) + dp(0, count + 1)
            else:
                res = dp(0, count + 1) + dp(1,count + 1 )
            
            memo[key] = res % mod
            return res % mod

        return dp(0, 0)
        