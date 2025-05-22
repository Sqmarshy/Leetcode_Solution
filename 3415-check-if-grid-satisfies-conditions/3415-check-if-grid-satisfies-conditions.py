class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            if r != 0:
                if grid[r] != grid[r - 1]:
                    return False
            for c in range(1, cols):
                if grid[r][c] == grid[r][c - 1]:
                    return False

        return True 