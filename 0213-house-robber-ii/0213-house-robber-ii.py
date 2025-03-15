class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {} 
        def dp(idx, limit):
            if idx >= limit:
                return 0

            if (idx, limit) in memo:
                return memo[(idx, limit)]
            
            if idx == 0:
                take = nums[idx] + dp(idx + 2, limit - 1)
                skip = dp(idx + 1, limit)
            else:
                take = nums[idx] + dp(idx + 2, limit)
                skip = dp(idx + 1, limit)

            res = max(take, skip)
            memo[(idx, limit)] = res
            return res

        result = dp(0, len(nums))
        return result