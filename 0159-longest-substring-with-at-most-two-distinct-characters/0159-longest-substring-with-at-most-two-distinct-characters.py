class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        count = Counter()
        res = 0
        for i in range(len(s)):
            count[s[i]] += 1
            if len(count) <= 2:
                res = max(res, (i - left + 1))
            else:
                while len(count) > 2:
                    curr = s[left]
                    count[curr] -= 1
                    if count[curr] == 0:
                        del count[curr]
                    left += 1
        return res