class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        dist = [0] * n

        # Right 
        curr = 0
        for r in range(n):
            if dominoes[r] == '.':
                if curr == 0: continue
                dist[r] += curr
                curr -= 1
            elif dominoes[r] == 'R':
                dist[r] = n
                curr = n - 1
            else:
                curr = 0

        # Left
        curr = 0
        for l in range(n - 1, -1, -1):
            if dominoes[l] == '.':
                if curr == 0: continue
                dist[l] += curr
                curr += 1
            elif dominoes[l] == 'L':
                dist[l] = -n
                curr = -(n - 1)
            else:
                curr = 0
        
        res = ['L' if d < 0 else 'R' if d > 0 else '.' for d in dist]
        return ''.join(res)