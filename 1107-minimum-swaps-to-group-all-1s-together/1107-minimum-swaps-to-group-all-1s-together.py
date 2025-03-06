class Solution:
    def minSwaps(self, data: List[int]) -> int:
        size = data.count(1)
        if not size:
            return 0
        res, curr = float('inf'), 0
        left = 0
        for i in range(len(data)):
            if i - left + 1 < size:
                if data[i] == 0:
                    curr += 1
                continue
            else:
                if data[i] == 0:
                    curr += 1
                res = min(res, curr)
                if data[left] == 0:
                    curr -= 1
                left += 1
        return res
                
