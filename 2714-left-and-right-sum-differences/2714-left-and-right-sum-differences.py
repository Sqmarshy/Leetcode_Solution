class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [], []
        for i in range(n):
            if i == 0:
                prefix.append(nums[i])
                suffix.append(nums[-(i + 1)])
                continue
            prefix.append(prefix[-1] + nums[i])
            suffix.append(suffix[-1] + nums[-(i + 1)])
        suffix.reverse()
        return [abs(prefix[i] - suffix[i]) for i in range(len(nums))]
