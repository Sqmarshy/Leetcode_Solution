class Solution:
    def minSwaps(self, data: List[int]) -> int:
        size = data.count(1)
        if not size:
            return 0
        res, curr = float('inf'), 0
        left = 0
        for i in range(len(data)):
            if i - left + 1 < size:
                curr += data[i]
                continue
            else:
                curr += data[i]
                res = min(res, size - curr)
                curr -= data[left]
                left += 1
        return res
                
