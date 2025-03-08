class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, 0
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set([(r,c)])
        res = [matrix[r][c]]
        while len(res) < rows*cols:
            for i, j in direction:
                while r + i >= 0 and r + i < rows and c + j >= 0 and c + j < cols and (r+i, c+j) not in visited:
                    r += i
                    c += j
                    visited.add((r,c))
                    res.append(matrix[r][c])
        return res