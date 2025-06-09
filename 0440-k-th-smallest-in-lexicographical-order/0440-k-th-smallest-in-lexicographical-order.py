class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(num):
            res = 0
            c = num
            adj = c + 1
            while c <= n:
                res += min(n+1,adj) - c
                c *= 10
                adj *= 10
            return res

        curr = 1
        while k > 1:
            steps = count(curr)
            if steps >= k: #inside this tree
                curr *= 10
                k -= 1
            else:
                curr += 1
                k -= steps
        return curr
