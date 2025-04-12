class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # Base case, if n only has 1 digit
        if n == 1:
            return len([i for i in range(1, 10) if i % k == 0])

        # Generating all possible Palindrome
        palin = []
        half = n // 2
        start = int(10 ** (half - 1))
        end = int(10 ** half - 1)
        if n % 2 == 1:
            for i in range(start, end + 1):
                left = str(i)
                right = left[::-1]
                for j in range(0, 10):
                    p = int(left + str(j) + right)
                    if p % k == 0:
                        palin.append(p)
        else:
            for i in range(start, end + 1):
                left = str(i)
                right = left[::-1]
                p = int(left + right)
                if p % k == 0:
                    palin.append(p)

        # Permutate all possible Palindrome to get nums it can form
        # Kept a visited set to avoid double-checking same digit distribution
        res = 0
        visited = set()
        for i in palin:
            s = str(i)
            check = ''.join(sorted(s))
            if check in visited:
                continue
            visited.add(check)
            digits = len(s)
            count = Counter(s)
            
            # All possible permute
            val = factorial(digits)
            for _, c in count.items():
                if c >= 2:
                    val /= factorial(c)
            
            # The ones with leading 0 like 012
            if '0' in count:
                count['0'] -= 1
                val_0 = factorial(digits - 1)
                for _, c in count.items():
                    if c >= 2:
                        val_0 /= factorial(c)
                val -= val_0
            res += val
        return int(res)