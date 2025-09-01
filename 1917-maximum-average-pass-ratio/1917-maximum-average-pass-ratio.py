class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        new = [[-((classes[i][0] + 1) /(classes[i][1] + 1) - (classes[i][0])/(classes[i][1])), classes[i][0], classes[i][1]] for i in range(len(classes))]
        heapq.heapify(new)
        for _ in range(extraStudents):
            curr = heapq.heappop(new)
            curr[1] = curr[1] + 1
            curr[2] = curr[2] + 1
            curr[0] = -((curr[1] + 1)/(curr[2] + 1) - curr[1]/curr[2])
            heapq.heappush(new, curr)
        
        return sum(i[1]/i[2] for i in new) / len(classes)

