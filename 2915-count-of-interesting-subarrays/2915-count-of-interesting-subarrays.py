class Solution:
    def countInterestingSubarrays(self, nums: List[int], mod: int, k: int) -> int:
        n = len(nums)
        count = Counter([0])
        curr = 0

        res = 0
        for num in nums:
            # Current total cnt
            if num % mod == k: curr += 1
            
            # (curr - x) % mod == k
            # (curr - x) - c*mod == k
            # (curr - x) == k + c*mod
            # x == curr - k - c*mod
            # x + k == curr % mod
            # x == curr % mod - k
            res += count[(curr - k + mod) % mod]
            count[curr % mod] += 1
        return res

