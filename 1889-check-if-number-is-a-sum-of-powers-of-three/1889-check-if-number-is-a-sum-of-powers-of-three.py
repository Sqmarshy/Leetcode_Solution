class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        k = 14
        while k >= 0:
            if n >= 3 ** k:
                n -= 3 ** k
            k -= 1
        return n == 0