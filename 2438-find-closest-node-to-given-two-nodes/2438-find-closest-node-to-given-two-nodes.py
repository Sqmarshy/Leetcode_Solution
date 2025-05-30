class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dic = defaultdict(list)
        for start, end in enumerate(edges):
            if end == -1:
                continue
            dic[start].append(end)

        min_dist_node1 = [float('inf')] * n 
        min_dist_node2 = [float('inf')] * n
        heap1 = [[0, node1]]
        heap2 = [[0, node2]]

        while heap1:
            dist, node = heapq.heappop(heap1)
            if min_dist_node1[node] != float('inf'):
                continue
            min_dist_node1[node] = dist

            for neighbour in dic[node]:
                if min_dist_node1[neighbour] == float('inf'):
                    heapq.heappush(heap1, [dist + 1, neighbour])
        
        while heap2:
            dist, node = heapq.heappop(heap2)
            if min_dist_node2[node] != float('inf'):
                continue
            min_dist_node2[node] = dist

            for neighbour in dic[node]:
                if min_dist_node2[neighbour] == float('inf'):
                    heapq.heappush(heap2, [dist + 1, neighbour])

        idx, res = -1, float('inf')
        for i in range(n):
            if type(min_dist_node1[i]) == int and type(min_dist_node2[i]) == int:
                k = max(min_dist_node1[i], min_dist_node2[i])
                if res > k:
                    res, idx = k, i
        return idx