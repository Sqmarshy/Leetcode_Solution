class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0].copy())
        for i in nums[1:]:
            k = set(i)
            res = res.intersection(k)
        return sorted(res)
            