class Solution:    
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7

        # First set elements for the unrestricted positions
        # E.g : res = [1, 2, 3, 4, 5] n = 8, k = 3
        unrestricted = pow(m - 1, n - k - 1, mod)

        # Put in the k element to be the same as prev position
        # E.g : res = [1, 2, 2* 3, 3*,3* 4, 5] n = 8, k = 3
        groups = comb(n - 1, k)
        return m * unrestricted * groups % mod
