class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = max(nums)
        if res < 0: return res

        curr = [i for i in nums if i > 0]
        res = sum(set(curr))
        return res
        
        # track = set()
        # for i in range(len(nums)):
        #     if nums[i] <= 0:
        #         continue
                
        #     if nums[i] not in track:
        #         curr += nums[i]
        #         track.add(nums[i])
        #     else:
        #         while nums[i] in track:
        #             curr -= nums[left]
        #             track.remove(nums[left])
        #             left += 1
        #         curr += nums[i]
        #         track.add(nums[i])
    
        #     res = max(res, curr)
        # return res