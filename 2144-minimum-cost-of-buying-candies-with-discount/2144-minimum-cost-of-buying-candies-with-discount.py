class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        res, k = 0, 0
        for i in cost:
            if k < 2:
                res += i
                k += 1
            else:
                k = 0
        return res