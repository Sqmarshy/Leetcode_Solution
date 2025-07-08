class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        events.append([9999999999, 9999999999, 0])
        n = len(events)
        memo = [[-1 for i in range(k + 1)] for _ in range(n)]
        def dp(idx, count):
            if idx >= n or count == 0:
                return 0

            if memo[idx][count] != -1:
                return memo[idx][count]

            left, right = idx + 1, n - 1
            while left < right:
                mid = (left + right) // 2
                if events[mid][0] <= events[idx][1]:
                    left = mid + 1
                else:
                    curr = right
                    right = mid

            take = dp(left, count - 1) + events[idx][2]
            ignore = dp(idx + 1, count)

            res = max(take, ignore)
            memo[idx][count] = res
            return res

        return dp(0, k)

