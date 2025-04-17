class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        nums_idx = [(nums[i], i) for i in range(len(nums))]
        nums_idx.sort()
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums_idx[i][0] == nums_idx[j][0]:
                    idx1, idx2 = nums_idx[i][1], nums_idx[j][1]
                    if (idx1 * idx2) % k == 0:
                        res += 1
                else:
                    break
        return res