class Solution:
    def confusingNumber(self, n: int) -> bool:
        if n == 0 :
            return False
        s = [i for i in str(n)]
        res = []
        can = {
            '1':'1', 
            '0':'0', 
            '6':'9', 
            '8':'8', 
            '9':'6'}
        for i in range(len(s) - 1, -1, -1):
            if not res and s[i] == '0':
                continue
            if s[i] in can:
                res.append(can[s[i]])
            else:
                return False

        return int(''.join(res)) != n
