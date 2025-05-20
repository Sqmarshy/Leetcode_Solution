class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        track = [0] * n
        for start, end in queries:
            track[start] += 1
            if end != n - 1:
                track[end + 1] -= 1

        curr = 0
        for idx, i in enumerate(track):
            curr += i
            if curr < nums[idx]:
                return False
        return True