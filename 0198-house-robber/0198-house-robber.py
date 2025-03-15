class Solution:
    def rob(self, nums: List[int]) -> int:
        # Bottom Up Tabulation
        if len(nums) <= 2:
            return max(nums)
        res = [0] * len(nums)
        res[0], res[1] = nums[0], nums[1]
        for i in range(2, len(nums)):
            res[i] = max(res[i - 2] + nums[i], res[i - 1])
        return res[-1]

        # Top down memoization
        memo = {}
        def dp(idx):
            # Look for past resule
            if idx in memo:
                return memo[idx]

            # Base case
            if idx >= len(nums):
                return 0
            
            # Making choices
            take = dp(idx + 2) + nums[idx]
            skip = dp(idx + 1)
            
            res = max(take, skip)
            memo[idx] = res
            return res
        return dp(0)