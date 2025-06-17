class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        dig = [int(i) for i in str(n)]
        prod = 1
        for i in dig:
            prod *= i
        return prod - sum(dig)