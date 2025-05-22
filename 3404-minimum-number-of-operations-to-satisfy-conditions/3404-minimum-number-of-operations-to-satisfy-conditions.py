class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        res_row = [[rows] * 10 for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                num = grid[r][c]
                res_row[c][num] -= 1
    
        memo = {}
        def dp(idx, prev):
            key = (idx, prev)
            if idx >= len(res_row):
                return 0
            if key in memo:
                return memo[key]
            
            res = float('inf')
            for number, count in enumerate(res_row[idx]):
                if number == prev: continue
                res = min(res, dp(idx + 1, number) + count)
            
            memo[key] = res
            return res
        
        return dp(0, 10)
            

