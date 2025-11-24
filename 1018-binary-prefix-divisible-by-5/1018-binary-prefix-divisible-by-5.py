class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        num = 0
        for i in range(len(nums)):
            num *= 2
            num += nums[i]
            num %= 5
            if num == 0:
                res.append(True)
            else:
                res.append(False)
        return res