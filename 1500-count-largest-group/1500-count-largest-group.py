class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = Counter()
        for i in range(1, n + 1):
            digit_sum = sum(int(x) for x in str(i))
            count[digit_sum] += 1
        maxi = max(count.values())
        res = sum(1 for i in count.values() if i == maxi)
        return res