class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        maxi, idx = -float('inf'), 0
        greater = [False] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if maxi > nums[i]:
                greater[i] = idx
            if nums[i] > maxi:
                idx = i
                maxi = nums[i]

        mini = float('inf')
        for i in range(len(nums)):
            if nums[i] > mini:
                if greater[i]:
                    return True
            else:
                mini = nums[i]
        return False
        