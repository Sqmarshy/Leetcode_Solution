class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        # Line Sweep helper function for O(q + n) compare array
        def line_sweep(query_end):
            up_down = [0] * (n + 1)
            for q in queries[:query_end]:
                start, end, val = q
                up_down[start] += val
                up_down[end + 1] -= val
            
            curr = 0
            for i in range(n):
                curr += up_down[i]
                if nums[i] - curr > 0:
                    return False
            return True
        
        # Reject case
        if not line_sweep(len(queries)):
            return -1

        # Binary Search for ending index
        left, right = 0, len(queries)
        while left < right:
            mid = (left + right) // 2
            if line_sweep(mid):
                right = mid
            else:
                left = mid + 1
        
        return right