class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        rows = len(image)
        cols = len(image[0])
        min_x, max_x = x, x
        min_y, max_y = y, y
        visited = set()

        def dfs(r, c):
            nonlocal min_x, max_x, min_y, max_y
            if r < 0 or c < 0 or c >= cols or r >= rows:
                return
            if (r, c) in visited or image[r][c] == "0":
                return
            
            visited.add((r, c))
            min_x = min(r, min_x)
            min_y = min(c, min_y)
            max_x = max(r, max_x)
            max_y = max(c, max_y)

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
            return
        
        dfs(x, y)
        return (max_x - min_x + 1) * (max_y - min_y + 1)
             