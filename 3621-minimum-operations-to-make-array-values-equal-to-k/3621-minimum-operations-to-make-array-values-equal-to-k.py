class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if k > min(nums):
            return -1
        res = 0
        for i in set(nums):
            if i > k:
                res += 1
        return res