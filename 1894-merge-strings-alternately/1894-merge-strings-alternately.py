class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        l1 = list(word1)
        l2 = list(word2)
        while l1 and l2:
            a, b = l1.pop(0), l2.pop(0)
            res.append(a)
            res.append(b)
        if l1:
            return ''.join(res) + ''.join(l1)
        elif l2:
            return ''.join(res) + ''.join(l2)
        else:
            return ''.join(res)