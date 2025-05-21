class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        r_change = set()
        c_change = set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    r_change.add(r)
                    c_change.add(c)
        
        for r in r_change:
            matrix[r] = [0 for _ in range(cols)]
        
        for c in c_change:
            for r in range(rows):
                matrix[r][c] = 0
        