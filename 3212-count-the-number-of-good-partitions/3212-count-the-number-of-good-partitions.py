class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        mod = 10**9 + 7 
        dic = {}
        for idx, num in enumerate(nums):
            if num in dic:
                dic[num].append(idx)
            else:
                dic[num] = [idx]
        
        intervals = [(dic[i][0], dic[i][-1]) for i in dic]
        count = 0
        latest = intervals[0][1]
        for start, end in intervals[1:]:
            if start > latest:
                count += 1
                latest = end
            else:
                latest = max(latest, end)
        return pow(2, count, mod)
            

