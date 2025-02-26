class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        cache = {}
        rows = len(grid)
        cols = len(grid[0])
        def dp(row, pos1, pos2):
            if pos1 < 0 or pos1 >= cols or pos2 < 0 or pos2 >= cols:
                return -10000
            if (row, pos1, pos2) in cache:
                return cache[(row, pos1, pos2)]

            if pos1 == pos2:
                curr = grid[row][pos1]
            else:
                curr = grid[row][pos1] + grid[row][pos2]

            if row == rows - 1:
                cache[(row, pos1, pos2)] = curr
                return curr

            choices = []
            for i in range(-1, 2):
                 for j in range(-1, 2):
                    choice = dp(row + 1, pos1 + i, pos2 + j)
                    if choice >= 0:
                        choices.append(choice)
            
            res = max(choices) + curr
            cache[(row, pos1, pos2)] = res
            return res
            
        return dp(0, 0, cols-1)