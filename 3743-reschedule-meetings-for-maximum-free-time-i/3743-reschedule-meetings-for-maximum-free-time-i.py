class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # Variables
        free = []
        prev = 0

        # All gaps between 2 events
        # 0 is included as well as it denote there is an extra event there to be shifted
        for i in range(len(startTime)):
            curr = startTime[i] - prev
            free.append(curr)
            prev = endTime[i]
        free.append(eventTime - prev)

        # Since relative order need to be preserved, sliding window can be used
        res = max(free) if free else 0
        temp, left = 0, 0
        for i in range(len(free)):
            if i - left + 1 < k + 1:
                temp += free[i]
                continue
            temp += free[i]
            res = temp if temp > res else res
            temp -= free[left]
            left += 1
        
        return res if res > temp else temp