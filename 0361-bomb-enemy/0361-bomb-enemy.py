class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def bomb(point):
            count = 0
            for dr, dc in dirs:
                r, c = point
                while r < rows and c < cols and r >= 0 and c >= 0 and grid[r][c] != "W":
                    if grid[r][c] == 'E':
                        count += 1
                    r, c = r + dr, c + dc
            return count

        res = 0
        cache = [[0 for i in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '0':
                    continue
                if (r == 0 or c == 0) or (grid[r - 1][c] != '0' or grid[r][c - 1] != '0' or grid[r - 1][c - 1] != '0'):
                    cache[r][c] = bomb((r,c))
                else:
                    cache[r][c] = cache[r - 1][c] + cache[r][c - 1] - cache[r - 1][c - 1]
                res = max(res, cache[r][c])
        return res

