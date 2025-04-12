class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        used_prefix = set()
        for i in range(n - 2):
            for j in range(i + 1, n - 2):
                if (nums[i], nums[j]) in used_prefix:
                    continue
                used_prefix.add((nums[i], nums[j]))
                left = j + 1
                right = n - 1
                while left < right:
                    curr = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr < target:
                        left += 1
                    elif curr > target:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        original_left, original_right = nums[left], nums[right]
                        while left < n and nums[left] == original_left:
                            left += 1
                        while right > left and nums[right] == original_right:
                            right -= 1
        return res