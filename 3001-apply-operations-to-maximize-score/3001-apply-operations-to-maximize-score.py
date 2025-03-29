import math
import heapq
from collections import defaultdict

class Solution:
    def maximumScore(self, nums, k):
        mod = 10**9 + 7
        n = len(nums)
        
        prime_scores = [0] * n
        memo = {}
        
        def calculate_prime_score(num):
            if num in memo:
                return memo[num]

            score = 0
            orig_num = num  
            for factor in range(2, int(math.sqrt(num)) + 1):
                if num % factor == 0:
                    score += 1
                    while num % factor == 0:
                        num //= factor

            if num > 1: 
                score += 1
            memo[orig_num] = score
            return score
        
        for i in range(n):
            prime_scores[i] = calculate_prime_score(nums[i])
        
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        right = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        operations = []
        for i in range(n):
            count = (i - left[i]) * (right[i] - i)
            operations.append((-nums[i], count))
        
        operations.sort()
        
        result = 1
        for neg_val, count in operations:
            val = -neg_val
            ops = min(count, k)
            if ops > 0:
                result = (result * pow(val, ops, mod)) % mod
                k -= ops
            
            if k == 0:
                break
                
        return result