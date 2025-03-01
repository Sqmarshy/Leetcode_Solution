class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        count , res = 0, []
        while nums:
            num = nums.pop(0)
            if num == 0:
                count += 1
            elif nums and num == nums[0]:
                res.append(2 * num)
                nums.pop(0)
                count += 1
            elif not nums:
                res.append(num)
            else:
                res.append(num)
        return res + [0] * count