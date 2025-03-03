class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        res = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            while count >= 2:
                if nums[left] == 0:
                    count -= 1
                left += 1
            res = res if res > (i - left + 1) else i - left + 1
        return res