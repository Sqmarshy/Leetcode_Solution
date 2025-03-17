class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            curr = nums[i]
            while left < right:
                if curr + nums[left] + nums[right] > 0:
                    right -= 1
                elif curr + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
        return [i for i in res]