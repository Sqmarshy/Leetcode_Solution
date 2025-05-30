class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dic = defaultdict(list)
        for start, end in enumerate(edges):
            if end == -1:
                continue
            dic[start].append(end)

        def dijkstra(starting_node):
            min_dist_node = [float('inf')] * n 
            heap = [[0, starting_node]]

            while heap:
                dist, node = heapq.heappop(heap)
                if min_dist_node[node] != float('inf'):
                    continue
                min_dist_node[node] = dist

                for neighbour in dic[node]:
                    if min_dist_node[neighbour] == float('inf'):
                        heapq.heappush(heap, [dist + 1, neighbour])
            
            return min_dist_node

        from_node1 = dijkstra(node1)
        from_node2 = dijkstra(node2)
        idx, res = -1, float('inf')
        for i in range(n):
            if type(from_node1[i]) == int and type(from_node2[i]) == int:
                k = max(from_node1[i], from_node2[i])
                if res > k:
                    res, idx = k, i
        return idx