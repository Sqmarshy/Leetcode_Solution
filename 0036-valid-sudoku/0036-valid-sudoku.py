class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = cols = 9
        # Rows
        for r in range(rows):
            track = set()
            for c in range(cols):
                if board[r][c] != '.' and board[r][c] in track:
                    print(1)
                    return False
                track.add(board[r][c])
        
        # Cols
        for c in range(cols):
            track = set()
            for r in range(rows):
                if board[r][c] != '.' and board[r][c] in track:
                    print(2)
                    return False
                track.add(board[r][c])
        
        # Box
        for br in range(3):
            for bc in range(3):
                track = set()
                for r in range(3):
                    for c in range(3):
                        if board[r + 3 * br][c + 3 * bc] != '.' and board[r + 3 * br][c + 3 * bc] in track:
                            return False
                        track.add(board[r + 3 * br][c + 3 * bc])
        
        return True