class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def helper(cap):
            idx, count = 0, 0
            while idx < len(nums):
                if nums[idx] <= cap:
                    count += 1
                    idx += 2
                else:
                    idx += 1
            return count >= k
        
        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        return right