class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = []
        curr, left = 0, 0
        for i in range(n):
            curr += nums[i]
            if i - left + 1 < k:
                continue
            prefix.append(curr)
            curr -= nums[left]
            left += 1
        
        res = max(prefix)
        seen = set()
        for i in range(len(prefix)):
            if i in seen or prefix[i] < 0:
                continue
            
            num = prefix[i]
            count = i
            while count + k < len(prefix):
                count += k
                num += prefix[count]
                seen.add(count)
                res = max(num, res)
                if num < 0:
                    break
            res = max(num, res)

        return res
