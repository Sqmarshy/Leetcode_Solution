class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 2 * (n**2 - n) 