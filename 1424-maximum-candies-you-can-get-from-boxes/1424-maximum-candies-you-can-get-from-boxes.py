class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        bfs = deque(initialBoxes.copy())
        cant_open = set([i for i in range(len(status)) if status[i] != 1])
        for idx, box in enumerate(keys):
            for key in box:
                if key != idx and key in cant_open:
                    cant_open.remove(key)
        res = 0
        while bfs:
            curr = bfs.popleft()
            if status[curr] == 0:
                if curr not in cant_open:
                    bfs.append(curr)
                continue
            for box in containedBoxes[curr]:
                bfs.append(box)
            for key in keys[curr]:
                status[key] = 1
            res += candies[curr]
        return res