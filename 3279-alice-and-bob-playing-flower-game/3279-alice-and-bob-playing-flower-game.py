class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        res = 0
        odd = math.ceil(m / 2)
        even = m // 2

        for i in range(1, n + 1):
            if i % 2 == 0:
                res += odd
            else:
                res += even
        
        return res