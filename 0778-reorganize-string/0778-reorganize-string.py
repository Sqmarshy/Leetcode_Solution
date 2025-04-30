class Solution:
    def reorganizeString(self, s: str) -> str:
        idx, n = 0, len(s)
        res = [''] * n
        sorted_s = sorted(s, key = lambda x: [-s.count(x), x])
        for i in range(0, n, 2):
            res[i] = sorted_s[idx]
            idx += 1
        
        for i in range(1, n, 2):
            res[i] = sorted_s[idx]
            idx += 1
            if (i != n - 1) and (res[i] == res[i - 1] or res[i] == res[i + 1]):
                return ''
        
        return ''.join(res)
