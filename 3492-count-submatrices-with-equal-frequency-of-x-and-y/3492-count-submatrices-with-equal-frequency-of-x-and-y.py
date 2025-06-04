class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        prefix = [[[0,0,0] for i in range(cols)] for _ in range(rows)]
        helper = {'X' : 0, 'Y' : 1, '.':2}
        for r in range(rows):
            for c in range(cols):
                letter = grid[r][c]
                idx = helper[letter]
                if (r == 0 and c == 0):
                    prefix[r][c][idx] += 1
                elif r == 0:
                    prefix[r][c] = prefix[r][c - 1].copy()
                    prefix[r][c][idx] += 1
                elif c == 0:
                    prefix[r][c] = prefix[r - 1][c].copy()
                    prefix[r][c][idx] += 1
                else:
                    prefix[r][c][0] = prefix[r][c - 1][0] + prefix[r - 1][c][0] - prefix[r - 1][c -1][0] 
                    prefix[r][c][1] = prefix[r][c - 1][1] + prefix[r - 1][c][1] - prefix[r - 1][c -1][1] 
                    prefix[r][c][idx] += 1

                if prefix[r][c][0] >= 1 and prefix[r][c][0] == prefix[r][c][1]:
                    res += 1
        return res