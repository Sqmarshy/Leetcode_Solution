class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # Preparation
        n = len(nums)
        queries.sort(key = lambda x: [x[0], x[1]])

        # Defining variables for solution
        size = len(queries)
        diff = [0] * (len(nums) + 1)
        left, curr = 0, 0
        res = []

        # Main Iteration
        for i, num in enumerate(nums):
            curr += diff[i]
            while left < size and queries[left][0] <= i:
                heappush(res, -queries[left][1])
                left += 1
            
            while res and curr < num and -res[0] >= i:
                curr += 1
                temp = -heapq.heappop(res)
                diff[temp + 1] -= 1

            if curr < num: 
                return -1
            
        return len(res)