class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        sample = Counter([i for i in range(1, n**2 + 1)])
        res = [0, 0]
        sum_ = 0
        for r in range(n):
            for c in range(n):
                num = grid[r][c]
                sum_ += num
                if sample[num] == 0:
                    res[0] = num
                sample[num] -= 1
        
        for i in sample:
            if sample[i] == 1:
                res[1] = i
                return res