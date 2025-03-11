class Solution:
    def maxScore(self, nums: List[int]) -> int:
        pos = [i for i in nums if i > 0]
        neg = [i for i in nums if i <= 0]
        total = sum(pos)
        neg.sort(reverse = True)
        res = len(pos)
        for i in neg:
            total += i
            if total > 0:
                res += 1
            else:
                return res
        return res
