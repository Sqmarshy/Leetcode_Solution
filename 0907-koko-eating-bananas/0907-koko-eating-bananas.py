class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def to_eat(k):
            res = 0
            for pile in piles:
                if k >= pile:
                    res += 1
                else:
                    res += math.ceil(pile / k)
            return res <= h
        
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if to_eat(mid):
                right = mid
            else:
                left = mid + 1
        return left