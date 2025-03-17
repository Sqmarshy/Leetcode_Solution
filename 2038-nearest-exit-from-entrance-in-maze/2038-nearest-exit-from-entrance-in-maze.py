class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        bfs = deque([entrance])
        visited = set()
        res = 0
        while bfs:
            n = len(bfs)
            for _ in range(n):
                # Get the node and check if it is visited
                r, c = bfs.popleft()
                if (r, c) in visited:
                    continue
                visited.add((r, c))

                # Check if curr position is an exit
                if [r, c] != entrance and (r == rows - 1 or c == cols - 1 or r == 0 or c == 0):
                    return res

                # Increase search space
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue
                    if maze[nr][nc] == '+' or (nr, nc) in visited:
                        continue
                    bfs.append((nr, nc))
                
            # Increase step count
            res += 1
        return -1
                
                
