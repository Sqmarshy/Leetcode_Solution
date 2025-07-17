class Solution:
    def minimumKeypresses(self, s: str) -> int:
        count = Counter(s)
        val = sorted(count.values(), reverse = True)
        res, used = 0, 0
        for i in val:
            curr = used // 9 + 1
            res += curr * i
            used += 1
        return res