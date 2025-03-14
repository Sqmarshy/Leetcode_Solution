class Solution:
    def findIntegers(self, n: int) -> int:
        fib = [1,2]  # total 32 bits so get 32 fibs
        for i in range(30):  # more 30
            fib.append(fib[-1]+fib[-2])
            
        prev1Pos = float('inf')
        res = 0
        for i in range(31,-1,-1):
            if n & (1<<i) :
                res += fib[i]
                if i+1 == prev1Pos :  # ...i+1,i...0   
                    res -= 1   # ignore the +1 in res last
                    break
                prev1Pos = i
        return res + 1