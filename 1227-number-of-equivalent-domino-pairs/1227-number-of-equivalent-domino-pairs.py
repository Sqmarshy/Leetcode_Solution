class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return sum(sum(i for i in range(1, v)) if v >= 2 else 0 for v in Counter([tuple(sorted(i)) for i in dominoes]).values())
