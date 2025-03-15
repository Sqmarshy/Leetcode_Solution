class Solution:
    def rob(self, nums: List[int]) -> int:
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