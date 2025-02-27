class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        res = 0
        lookup = set(arr)
        memo = {}
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                curr = 2
                n1, n2 = arr[i], arr[j]

                while n1 + n2 in lookup:
                    if (n1, n2) in memo:
                        curr += memo[(n1, n2)] - 1
                        break
                    memo[(n1, n2)] = curr
                    n1, n2 = n2, n1 + n2
                    curr += 1
                res = res if res > curr else curr
        return res if res >= 3 else 0
