class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        count = Counter(word)
        freq = sorted(i for i in count.values())
        
        res = float('inf')
        curr_sum = 0
        for i in freq:
            curr = curr_sum
            for j in freq[::-1]:
                c = abs(i - j)
                if c > k:
                    curr += (c - k)
                else:
                    break
            res = min(res, curr)
            curr_sum += i
        return res