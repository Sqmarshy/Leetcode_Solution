class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0

        # First child can either take up to n or up to limit
        for i in range(min(limit, n) + 1):
            remain = n - i
            if remain > limit * 2:
                continue # At least one of the 2 remaining child will get > limit candies
            second_min = max(0, remain - limit) # if remain < limit, second child can get any amt <= limit
            second_max = min(remain, limit) # Second child can take up to remain or limit, whichever is smaller
            count = second_max - second_min + 1 # Formula to count number of item
            res += count
        
        return res


