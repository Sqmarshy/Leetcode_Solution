class Solution:
    def compare(self, s1, s2):
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                return False
        return True
    
    def colorTheGrid(self, m: int, n: int) -> int:
        rows = n # Change the orientation so its easier to generate a state
        cols = m
        mod = 10 ** 9 + 7

        # Generate all possibility
        single_row = set()
        possible = ['0', '1', '2']
        temp = [-1] * cols
        def backtrack(idx, prev):
            if idx == len(temp):
                single_row.add(''.join(temp.copy()))
                return
            
            for color in possible:
                if not prev or color != prev:
                    temp[idx] = color
                    backtrack(idx + 1, color)
                    temp[idx] = -1
                else:
                    continue
        backtrack(0, None)

        # DP to see which rows can go below each other
        memo = {}
        def dp(curr, prev):
            key = (curr, prev)
            if key in memo:
                return memo[key]
            if curr >= rows:
                return 1
            
            res = 0
            for r in single_row:
                if not prev:
                    res += dp(curr + 1, r)
                else:
                    satisfy = self.compare(prev, r)
                    res += dp(curr + 1, r) if satisfy else 0
            
            memo[key] = res % mod
            return res % mod
        
        return dp(0, None) % mod

