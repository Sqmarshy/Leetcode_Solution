class Solution:
    def isprime(self, num: int) -> bool:
        if num < 2:
            return False
        if num == 2:
            return True
        upper = int(num**0.5) + 1
        for i in range(3, upper, 2):
            if num % i == 0:
                return False
        return True

    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Only prime number pair who has a gap of 1 is 2 and 3
        if left <= 2 and right >= 3:
            return [2, 3]

        diff = float("inf")
        prev = 0
        res = [-1, -1]
        left = left + 1 if left % 2 == 0 else left
        for i in range(left, right + 1, 2):
            if self.isprime(i):
                curr_diff = i - prev
                if curr_diff < diff:
                    res[0], res[1] = prev, i
                    if curr_diff <= 2:
                        return res
                diff = curr_diff
                prev = i
        return res if res.count(0) == 0 else [-1, -1]
