class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def helper(limit):
            res = 0
            for candy in candies:
                res += candy // limit
                if res >= k:
                    return True
            return res >= k
        
        left = 1
        right = 10**7
        while left <= right:
            mid = (left + right) // 2
            if helper(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left if helper(left) else left - 1
