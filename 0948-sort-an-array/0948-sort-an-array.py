class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums

        left = self.sortArray(nums[:n // 2])
        right = self.sortArray(nums[n // 2:])

        res = []
        while left and right:
            if left[0] <= right[0]:
                num = left.pop(0)
            else:
                num = right.pop(0)
            res.append(num)
        
        remain = max(left, right, key = lambda x: len(x))
        return res + remain
