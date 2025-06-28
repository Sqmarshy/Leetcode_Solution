class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        lis = sorted([(nums[i], i) for i in range(len(nums))], reverse = True)[:k]
        res = [i[0] for i in sorted(lis, key = lambda x: x[1])]
        return res