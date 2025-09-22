class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        freq = Counter(count.values())
        res = 0
        for k, v in freq.items():
            res = max(res, k)
        return res * freq[res]