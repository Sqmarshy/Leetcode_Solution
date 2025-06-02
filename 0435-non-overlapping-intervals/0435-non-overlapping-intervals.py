class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key = lambda x: (x[1],x[0]))
        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                if res[-1][1] <= interval[0]:
                    res.append(interval)
        return n - len(res)

                