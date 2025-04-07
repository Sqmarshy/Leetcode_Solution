class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2
        n = len(nums)
        
        cache = [[None for _ in range(target + 1)] for _ in range(n)]
        
        def dp(idx, curr_sum):
            if curr_sum == target:
                return True
            
            if curr_sum > target or idx >= n:
                return False
            
            if cache[idx][curr_sum] is not None:
                return cache[idx][curr_sum]
            
            take = dp(idx + 1, curr_sum + nums[idx])
            skip = dp(idx + 1, curr_sum)
            
            cache[idx][curr_sum] = take or skip
            return cache[idx][curr_sum]
        
        return dp(0, 0)