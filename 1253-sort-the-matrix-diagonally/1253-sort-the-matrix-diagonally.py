class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        for r_ in range(rows - 1, -1, -1):
            r, c = r_, 0
            to_sort = []
            while r < rows and c < cols:
                to_sort.append(mat[r][c])
                r += 1
                c += 1

            r, c = r_, 0
            to_sort.sort()
            while r < rows and c < cols:
                mat[r][c] = to_sort.pop(0)
                r += 1
                c += 1
        
        for c_ in range(cols):
            r, c = 0, c_
            to_sort = []
            while r < rows and c < cols:
                to_sort.append(mat[r][c])
                r += 1
                c += 1
            
            r, c = 0, c_
            to_sort.sort()
            while r < rows and c < cols:
                mat[r][c] = to_sort.pop(0)
                r += 1
                c += 1
        
        return mat