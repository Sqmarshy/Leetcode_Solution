class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n, s = len(dominoes), list(dominoes)
        L = [idx for idx in range(n) if s[idx] == 'L']
        R = [idx for idx in range(n) if s[idx] == 'R']
        visited = set()
        while L or R:
            for _ in range(len(L)):
                dom = L.pop(0)
                if (dom - 1 >= 0) and (s[dom - 1] == '.') and (dom - 1 not in visited):
                    if dom - 2 < 0 or s[dom - 2] != 'R':
                        L.append(dom - 1)
                        s[dom - 1] = 'L'
                    else:
                        visited.add(dom - 1)
            for _ in range(len(R)):
                dom = R.pop(0)
                if (dom + 1 < n) and (s[dom + 1] == '.') and (dom + 1 not in visited):
                    if dom + 2 <= n or dom + 2 != 'L':
                        R.append(dom + 1)
                        s[dom + 1] = 'R'
                    else:
                        visited.add(dom + 1)
        return ''.join(s)