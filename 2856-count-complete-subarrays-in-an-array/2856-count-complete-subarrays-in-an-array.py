class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n, left = len(nums), 0
        count, k = Counter(), len(set(nums))
        res = 0

        for right in range(n):
            count[nums[right]] += 1
            while len(count) == k:
                pop = nums[left]
                res += (n - right)
                count[pop] -= 1
                if count[pop] == 0:
                    del count[pop] 
                left += 1
        return res