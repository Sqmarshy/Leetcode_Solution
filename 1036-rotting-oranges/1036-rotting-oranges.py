class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Variables
        rows = len(grid)
        cols = len(grid[0])
        total_oranges = 0
        bfs = deque([]) 

        # Count number of oranges we have
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                if grid[r][c] == 2:
                    bfs.append((r, c))
                total_oranges += 1
        
        # BFS, no modification of original grid
        time = 0
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while bfs:
            n = len(bfs)
            for _ in range(n):
                # Process and check if cell visited
                r, c = bfs.popleft()
                visited.add((r, c))

                # Increase search space
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nc >= cols or nr >= rows:
                        continue
                    if grid[nr][nc] != 1 or (nr, nc) in visited:
                        continue
                    bfs.append((nr, nc))
                    visited.add((nr, nc))
                    
            # If there are new orange getting rotten, we need an extra step
            if bfs:
                time += 1
        return time if len(visited) == total_oranges else -1