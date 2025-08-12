class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7
        num, nums = 1, []
        while (num ** x) <= n:
            nums.append(num ** x)
            num += 1

        memo = [[-1 for i in range(n + 1)] for _ in range(len(nums))]
        def dp(idx, curr):
            if curr == 0:
                return 1
            if curr < 0:
                return 0
            if idx >= len(nums):
                return 0
            if memo[idx][curr] != -1:
                return memo[idx][curr]

            take = dp(idx + 1, curr - nums[idx]) 
            skip = dp(idx + 1, curr)
            res = take + skip
            memo[idx][curr] = res
            return res
        
        ret = dp(0, n)
        return ret % mod
            
