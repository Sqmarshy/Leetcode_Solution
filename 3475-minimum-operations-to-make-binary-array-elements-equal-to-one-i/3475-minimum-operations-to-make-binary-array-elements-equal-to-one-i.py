class Solution:
    def minOperations(self, nums: List[int]) -> int:
        left = 0
        res = 0
        for i in range(len(nums)):
            if i - left + 1 < 3:
                continue
            if nums[left] == 0:
                for j in range(left, i + 1):
                    nums[j] ^= 1
                res += 1
            left += 1
        return res if sum(nums) == len(nums) else -1
            