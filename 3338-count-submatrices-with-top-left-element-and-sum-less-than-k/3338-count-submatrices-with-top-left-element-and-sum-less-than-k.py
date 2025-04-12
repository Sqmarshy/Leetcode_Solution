class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        matrix = [[i for i in grid[j]] for j in range(len(grid))]
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    pass
                elif r == 0:
                    matrix[r][c] = matrix[r][c - 1] + grid[r][c]
                elif c == 0:
                    matrix[r][c] = matrix[r - 1][c] + grid[r][c]
                else:
                    matrix[r][c] = matrix[r - 1][c] + matrix[r][c - 1] + grid[r][c] - matrix[r - 1][c - 1]

                if matrix[r][c] <= k:
                    res += 1
        return res
        