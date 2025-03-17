class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(n & 1 == 0 for n in Counter(nums).values())