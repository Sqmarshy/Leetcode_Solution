class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        lis = [(nums[i], i) for i in range(len(nums))]
        lis.sort(reverse = True)
        lis = lis[:k]
        res = [i[0] for i in sorted(lis, key = lambda x: x[1])]
        return res