class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for start in points:
            count = Counter()
            for other in points:
                if start == other:
                    continue
                dist = (start[0] - other[0])**2 + (start[1] - other[1])**2
                count[dist] += 1
                res += 2 * (count[dist] - 1) # If only have 1 dist it will be 0
        return res
             
                