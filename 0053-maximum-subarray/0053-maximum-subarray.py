class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = nums[0]
        max_sub = nums[0]

        for i in nums[1:]:
            prefix = 0 if prefix < 0 else prefix
            prefix += i
            max_sub = prefix if prefix > max_sub else max_sub
    
        return max_sub