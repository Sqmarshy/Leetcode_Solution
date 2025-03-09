class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        res = 0
        left = 0
        track = Counter()
        for i in range(len(s)):
            track[s[i]] += 1
            if i - left + 1 >= k:           
                if len(track) == k:
                    res += 1
                track[s[left]] -= 1
                if track[s[left]] == 0:
                    del track[s[left]]
                left += 1
        return res