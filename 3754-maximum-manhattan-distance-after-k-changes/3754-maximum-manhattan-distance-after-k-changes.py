class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x, y = 0, 0
        res = 0
        n = len(s)
        for i in range(n):
            if s[i] == "N":
                y += 1
            elif s[i] == "S":
                y -= 1

            elif s[i] == "E":
                x += 1
            elif s[i] == "W":
                x -= 1
            res = max(res, min(abs(y) + abs(x) + k * 2, i + 1))
        return res