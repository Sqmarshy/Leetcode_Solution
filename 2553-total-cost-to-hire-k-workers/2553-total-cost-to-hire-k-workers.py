class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        first = costs[:candidates]
        last = costs[max(candidates, len(costs) - candidates):]
        heapq.heapify(first)
        heapq.heapify(last)
        left, right = candidates, len(costs) - candidates - 1
        res = 0
        while k:
            a = first[0] if first else 9999999
            b = last[0] if last else 9999999
            if a <= b:
                a = heapq.heappop(first)
                res += a
                if left <= right:
                    heapq.heappush(first, costs[left])
                    left += 1
            else:
                b = heapq.heappop(last)
                res += b
                if left <= right:
                    heapq.heappush(last, costs[right])
                    right -= 1
            k -= 1
        return res
