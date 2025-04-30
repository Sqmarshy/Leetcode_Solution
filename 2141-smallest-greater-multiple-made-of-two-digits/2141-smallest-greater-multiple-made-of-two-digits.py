class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        if digit1 == digit2 == 0 :
            return -1

        limit = 2**31 - 1
        visited = set()
        bfs = []
        bfs.append([str(min(digit1, digit2))])
        bfs.append([str(max(digit1, digit2))])
        while bfs:
            num = bfs.pop(0)
            s = ''.join(num)
            res = int(s)
            if s in visited or res > limit or res == 0:
                continue
            visited.add(s)
            if res > k and res % k == 0:
                return res
            bfs.append(num + [str(min(digit1, digit2))])
            bfs.append(num + [str(max(digit1, digit2))])
        return -1