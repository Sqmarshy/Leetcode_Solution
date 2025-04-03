class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        for i in range(1, n):
            left[i] = max(left[i - 1], nums[i - 1])
        for i in range(n-2, -1, -1):
            right[i] = max(right[i + 1], nums[i + 1])

        res = 0
        for j in range(1, n - 1):
            eqn = (left[j] - nums[j]) * right[j]
            res = max(res, eqn)
        return res
