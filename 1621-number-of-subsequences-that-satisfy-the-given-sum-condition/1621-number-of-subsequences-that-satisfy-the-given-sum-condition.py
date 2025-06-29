class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        nums.sort()

        res = 0
        for i in range(len(nums)):
            if nums[i] * 2 > target: continue

            left, right = i , len(nums) - 1
            while left < right:
                mid = ceil((left + right) / 2)
                if nums[i] + nums[mid] <= target:
                    left = mid
                else:
                    right = mid - 1
                
            # Find last possible idx to match current i
            # Fix the head and everything we can choose to take or not
            count = (left - i)
            res += pow(2, count, mod) if count != 0 else 1
            res %= mod
        
        return res % mod
            