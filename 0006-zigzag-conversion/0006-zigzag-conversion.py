class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        res = [[] for i in range(numRows)]
        idx, side = 0, 1
        for i in s:
            res[idx].append(i)
            if idx + side >= numRows or idx + side < 0:
                side *= -1
            idx += side

        final = []
        for row in res:
            for letter in row:
                final.append(letter)
        return ''.join(final) 