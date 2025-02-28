class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        memo = {}
        def lcs(i, j):
            if i >= len(str1):
                return ''
            if j >= len(str2):
                return ''
            if (i, j) in memo:
                return memo[(i, j)]

            if str1[i] == str2[j]:
                return lcs(i+1, j+1) + str1[i]
            else:
                first = lcs(i + 1, j)
                second = lcs(i, j + 1)

            res = first if len(first) > len(second) else second
            memo[(i, j)] = res
            return res

        dp = lcs(0, 0)[::-1]
        res = []
        idx1, idx2, dpi = 0, 0, 0
        while idx1 < len(str1) and idx2 < len(str2):
            if str1[idx1] == str2[idx2]:
                if dpi < len(dp) and str1[idx1] == dp[dpi]:
                    dpi += 1
                res.append(str1[idx1])
                idx1 += 1
                idx2 += 1
            elif dpi < len(dp) and str1[idx1] == dp[dpi]:
                res.append(str2[idx2])
                idx2 += 1
            elif dpi < len(dp) and str2[idx2] == dp[dpi]:
                res.append(str1[idx1])
                idx1 += 1
            else:
                res.append(str1[idx1])
                res.append(str2[idx2])
                idx1 += 1
                idx2 += 1
        
        if idx1 < len(str1):
            res.append(str1[idx1:])
        if idx2 < len(str2):
            res.append(str2[idx2:])

        return ''.join(res)