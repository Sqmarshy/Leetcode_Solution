class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def helper(force):
            min_next = 0
            k = 0
            for i in position:
                if i >= min_next:
                    k += 1
                    min_next = i + force
            return k >= m
        
        left = 1
        right = max(position)
        while left < right:
            mid = math.ceil((left + right) / 2)
            if helper(mid):
                left = mid
            else:
                right = mid - 1
        return left