class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums = [0 if i % 2 == 0 else 1 for i in nums]
        res = max(nums.count(0), nums.count(1))
        a, b = 1, 0
        c1, c2 = 0, 0
        for i in nums:
            if i == a:
                a ^= 1
                c1 += 1
            if i == b:
                b ^= 1
                c2 += 1
        return max(c1, c2, res)