class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if len(costs) == k:
            return sum(costs)

        first = [(costs[i], i) for i in range(candidates)]
        last = [(costs[i], i) for i in range(len(costs) - candidates, len(costs))]
        heapq.heapify(first)
        heapq.heapify(last)
        track = set()
        left, right = candidates, len(costs) - candidates - 1
        res = 0
        while k:
            a = first[0] if first else (9999999, len(costs))
            b = last[0] if last else (9999999, len(costs))
            if a < b:
                a = heapq.heappop(first)
                if a[1] in track:
                    continue
                res += a[0]
                track.add(a[1])
                if left <= right:
                    heapq.heappush(first, (costs[left], left))
                    left += 1
            else:
                b = heapq.heappop(last)
                if b[1] in track:
                    continue
                res += b[0]
                track.add(b[1])
                if left <= right:
                    heapq.heappush(last, (costs[right], right))
                    right -= 1
            k -= 1
        return res
