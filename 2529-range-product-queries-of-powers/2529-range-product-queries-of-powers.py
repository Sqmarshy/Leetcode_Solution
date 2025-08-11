class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        k = [2**j for j in range(32)]
        k.reverse()

        power = []
        for i in k:
            while n >= i:
                power.append(i)
                n -= i
        power.reverse()
        prefix = []
        for i in power:
            if not prefix:
                prefix.append(i)
            else:
                curr = prefix[-1] * i
                prefix.append(curr)
        
        res = []
        for start, end in queries:
            curr = prefix[end] * power[start] // prefix[start]
            curr %= mod
            res.append(curr)
        
        return res