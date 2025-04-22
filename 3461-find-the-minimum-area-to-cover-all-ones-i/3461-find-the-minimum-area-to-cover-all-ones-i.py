class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        min_x, min_y, max_x, max_y = 1001, 1001, 0, 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    min_x = r if r < min_x else min_x
                    min_y = c if c < min_y else min_y
                    max_x = r if r > max_x else max_x
                    max_y = c if c > max_y else max_y

        return (max_x - min_x + 1) * (max_y - min_y + 1)