class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1:
            return 1
        if k % 2 == 0:
            return -1

        seen = set()
        length = 2
        n1, n2 = 1 % k, 10 % k
        res = (n1 + n2) % k
        while res not in seen:
            if res == 0:
                return length
            seen.add(res)
            n2 = (n2 * 10) % k
            res += n2
            res %= k
            length += 1

        return -1
