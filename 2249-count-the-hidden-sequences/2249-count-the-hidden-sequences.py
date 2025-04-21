class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        up, down = 0, 0
        start = 0
        for i in differences:
            start += i
            up = max(up, start)
            down = min(down, start)

        diff = down - lower
        res = upper - (up - diff) + 1
        return res if res >= 0 else 0
