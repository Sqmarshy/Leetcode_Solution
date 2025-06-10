class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        res = nums[:2] + nums[-3:]
        first = res[0] * res[1] * res[-1]
        second = res[-1] * res[-2] * res[-3] 
        return max(first, second)