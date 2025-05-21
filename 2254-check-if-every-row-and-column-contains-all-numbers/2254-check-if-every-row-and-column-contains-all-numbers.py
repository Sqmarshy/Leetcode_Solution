class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows = cols = len(matrix)
        for r in matrix:
            if len(set(r)) != len(matrix):
                return False
        
        for r in range(rows):
            for c in range(r, cols):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for r in matrix:
            if len(set(r)) != rows:
                return False
        
        return True
