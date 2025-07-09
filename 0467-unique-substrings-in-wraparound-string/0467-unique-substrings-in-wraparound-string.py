class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if len(s) == 1:
            return 1

        res = 0
        memo = [0] * 26
        prev, curr = 0, 0
        for i in range(len(s) - 1, -1, -1):
            if not prev:
                memo[ord(s[i]) - ord('a')] = 1
                curr = 1
                prev = s[i]
                continue
            
            if (s[i] == 'z' and prev == 'a') or (ord(prev) - ord(s[i])) == 1:
                curr += 1
            else:
                curr = 1
            
            prev = s[i]
            memo[ord(s[i]) - ord('a')] = max(memo[ord(s[i]) - ord('a')], curr)
        
        return sum(memo)