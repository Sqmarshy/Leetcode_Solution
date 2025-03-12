class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        curr = 0
        pos = False
        for i in range(len(nums)):
            if nums[i] < 0:
                curr += 1
            elif nums[i] == 0:
                continue
            else:
                pos = True
                break
        return max(len(nums) - i, curr) if pos or curr else 0
