class Solution:
    def countGoodNumbers(self, n: int) -> int:
        res = 1
        mod = 10**9 + 7
        odd = (n // 2)
        even = (n - n // 2)
        res *= pow(5, even, mod)
        res *= pow(4, odd, mod)
        return res % mod