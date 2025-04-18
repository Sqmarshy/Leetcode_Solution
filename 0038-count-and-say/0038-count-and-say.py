class Solution:
    def countAndSay(self, n: int) -> str:
        memo = {}
        def compression(k):
            # Base Case and Cache Checking
            if k == 1:
                return '1'
            if k in memo: 
                return memo[k]
            
            # Strign Compression
            stack = []
            lis = compression(k - 1)
            curr, prev = 1, lis[0]
            for element in lis[1:]:
                if element == prev:
                    curr += 1
                else:
                    stack.append(str(curr))
                    stack.append(prev)
                    curr, prev = 1, element
                
            # Adding the final element
            stack.append(str(curr))
            stack.append(prev)
            final = ''.join(stack) 
            memo[k] = final
            return final
        return compression(n)