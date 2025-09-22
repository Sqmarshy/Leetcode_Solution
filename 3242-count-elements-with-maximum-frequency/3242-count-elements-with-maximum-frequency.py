class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        freq = Counter(count.values())
        res = max(freq.keys())
        return res * freq[res]