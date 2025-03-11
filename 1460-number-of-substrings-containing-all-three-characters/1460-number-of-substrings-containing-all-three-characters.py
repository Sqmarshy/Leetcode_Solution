class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        left = 0
        c_count = Counter()
        for i in range(len(s)):
            c_count[s[i]] += 1
            while len(c_count) == 3:
                res += len(s) - i
                
                c_count[s[left]] -= 1
                if c_count[s[left]] == 0:
                    del c_count[s[left]]
                left += 1
        return res