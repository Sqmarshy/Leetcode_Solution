class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        return sum(
            1 for i in range(2, len(nums))
            if nums[i - 2] + nums[i] == nums[i - 1] / 2)