class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        prev = nums[0]
        for i in nums:
            if prev + k < i:
                prev = i
                res += 1
        return res