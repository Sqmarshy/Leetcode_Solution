class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def helper(limit):
            res = 0
            for candy in candies:
                res += candy // limit
                if res >= k:
                    return True
            return res >= k
        
        if not helper(1):
            return 0

        left = 1
        right = max(candies)
        while left < right:
            mid = math.ceil((left + right) / 2)
            if helper(mid):
                left = mid
            else:
                right = mid - 1
        return left
