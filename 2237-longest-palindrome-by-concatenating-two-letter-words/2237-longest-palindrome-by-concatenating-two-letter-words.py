class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        track = Counter()
        res = 0
        for i in words:
            rev = i[::-1]
            if rev in track and track[rev] >= 1:
                res += 4
                track[rev] -= 1
            else:
                track[i] += 1
        
        for i, val in track.items():
            if i[0] == i[1] and val > 0:
                return res + 2
        
        return res