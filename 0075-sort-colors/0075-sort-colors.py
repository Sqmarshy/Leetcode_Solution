class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a, b, c = 0, 0, 0
        for i in nums:
            if i==0:
                a += 1
            elif i==1:
                b += 1
            else:
                pass
        for i in range(len(nums)):
            if a > 0:
                nums[i] = 0
                a -= 1
            elif b > 0:
                nums[i] = 1
                b -= 1
            else:
                nums[i] = 2
                