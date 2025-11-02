class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        rows = m
        cols = n
        matrix = [[0 for c in range(cols)] for _ in range(rows)]
        for wall in walls:
            matrix[wall[0]][wall[1]] = 'w'
        for guard in guards:
            matrix[guard[0]][guard[1]] = 'g'

        def guarded(guard):
            r, c = guard

            up = r - 1
            while up >= 0 and type(matrix[up][c]) == int:
                matrix[up][c] = 1
                up -= 1

            down = r + 1
            while down < rows and type(matrix[down][c]) == int:
                matrix[down][c] = 1
                down += 1

            left = c - 1
            while left >= 0 and type(matrix[r][left]) == int:
                matrix[r][left] = 1
                left -= 1

            right = c + 1
            while right < cols and type(matrix[r][right]) == int:
                matrix[r][right] = 1
                right += 1
        
        for guard in guards:
            guarded(guard)

        res = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    res += 1
        return res