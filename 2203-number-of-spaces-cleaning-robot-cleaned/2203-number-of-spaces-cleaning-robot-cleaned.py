class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        rows, cols = len(room), len(room[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = defaultdict(set)

        res = 0
        r, c, d = 0, 0, 0
        while d not in visited[(r, c)]:
            # Check if curr room is cleaned
            if room[r][c] == 0:
                res += 1
                room[r][c] = 2

            # Update direction state and set variables
            dr, dc = directions[d]
            nr, nc = r + dr, c + dc
            visited[(r, c)].add(d)

            # If next cell out of bound or hit wall, change direction
            if (nr < 0 or nr >= rows or nc < 0 or nc >= cols) or (room[nr][nc] == 1):
                d = (d + 1) % 4
                continue
            
            # Update current position and cleaned cell
            r, c = nr, nc
        
        return res