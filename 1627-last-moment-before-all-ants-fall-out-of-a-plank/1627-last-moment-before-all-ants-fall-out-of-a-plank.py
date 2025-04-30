class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max([l for l in left] + [abs(r - n) for r in right])
