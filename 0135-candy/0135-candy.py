class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        res = [1] * n
        total = 0
        queue = deque(sorted([(rate, i) for i, rate in enumerate(ratings)]))
        while queue:
            val, idx = queue.popleft()
            if idx == 0:
                left, right = ratings[idx], ratings[idx + 1]
            elif idx == n - 1:
                left, right = ratings[idx - 1], ratings[idx]
            else:
                left, right = ratings[idx - 1], ratings[idx + 1]
            
            if left < val and right < val:
                res[idx] = max(res[idx - 1], res[idx + 1]) + 1
            elif left < val:
                res[idx] = res[idx - 1] + 1 
            elif right < val:
                res[idx] = res[idx + 1] + 1
            
            total += res[idx]
        
        return total
            