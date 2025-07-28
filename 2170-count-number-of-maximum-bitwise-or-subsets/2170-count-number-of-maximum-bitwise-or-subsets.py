class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        val, res = 0, 0
        def backtrack(idx, curr):
            nonlocal val, res
            if curr > val:
                val, res = curr, 1
            elif curr == val:
                res += 1
            
            if idx == n:
                return 0
            
            for i in range(idx, n):
                new = curr | nums[i]
                backtrack(i+1, new)

        backtrack(0, 0)
        return res