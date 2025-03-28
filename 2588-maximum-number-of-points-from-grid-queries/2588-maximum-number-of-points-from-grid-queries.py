class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        rows, cols = len(grid), len(grid[0])
        uniq_query = sorted(set(queries))
        
        # BFS preparation
        bfs = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        curr = 0
        k_idx = 0
        cache = {}
        
        while bfs and k_idx < len(uniq_query):
            val, r, c = heapq.heappop(bfs)
            
            # If current cell's value >= current query value, update cache
            while k_idx < len(uniq_query) and uniq_query[k_idx] <= val:
                cache[uniq_query[k_idx]] = curr
                k_idx += 1
            
            curr += 1  
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(bfs, (grid[nr][nc], nr, nc))
        
        # Map back to original query order, use .get for query that has higher val than max(grid)
        return [cache.get(queries[i], curr) for i in range(n)]