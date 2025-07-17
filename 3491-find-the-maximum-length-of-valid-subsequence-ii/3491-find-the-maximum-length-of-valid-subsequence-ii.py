class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        nums = [i % k for i in nums]
        res = 0
        for i in range(k):
            curr = 0
            dp = [0] * k
            for j in range(len(nums) - 1, -1, -1):
                find = i - nums[j] if i >= nums[j] else (i + k) - nums[j] 
                dp[nums[j]] = dp[find] + 1
                curr = max(curr, dp[nums[j]])

            res = res if res > curr else curr
        return res
