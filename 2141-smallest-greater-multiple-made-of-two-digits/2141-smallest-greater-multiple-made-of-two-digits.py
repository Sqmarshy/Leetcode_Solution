class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        if digit1 == digit2 == 0 :
            return -1

        limit = 2**31 - 1
        mini, maxi = min(digit1, digit2), max(digit1, digit2)
        bfs, visited = [[str(mini)], [str(maxi)]], set()
        while bfs:
            num = bfs.pop(0)
            s = ''.join(num)
            res = int(s)
            if s in visited or res > limit or res == 0:
                continue
            visited.add(s)
            if res > k and res % k == 0:
                return res
            bfs.append(num + [str(mini)])
            bfs.append(num + [str(maxi)])
        return -1