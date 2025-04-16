class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        res = 0
        dic = {0:-1} #val : idx
        curr = 0
        for idx, num in enumerate(nums):
            curr += num
            diff = curr - k
            if diff in dic:
                start = dic[diff] + 1
                res = max(res, idx - start + 1)
            if curr not in dic:
                dic[curr] = idx
        return res