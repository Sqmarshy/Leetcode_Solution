class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        nums = [tuple(sorted(i)) for i in dominoes]
        count = Counter(nums)
        res = 0
        for k, v in count.items():
            if v >= 2:
                curr = sum(i for i in range(1, v))
                res += curr
        return res