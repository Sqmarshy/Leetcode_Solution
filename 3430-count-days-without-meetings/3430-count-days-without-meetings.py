class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        res, prev = 0, 0
        for start, end in meetings:
            res += max(0, start - prev - 1)
            prev = max(end, prev)
        res += max(0, days - prev)
        return res