class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        heap = []
        combind = [(nums1[i], nums2[i]) for i in range(len(nums1))]
        curr = 0
        combind.sort(key = lambda x: x[1], reverse = True)
        for i in range(len(combind)):
            if len(heap) < k:
                heapq.heappush(heap, combind[i][0])
                curr += combind[i][0]
                multiple = combind[i][1]
            else:
                res = res if multiple * curr < res else multiple * curr 
                if heap[0] < combind[i][0]:
                    curr -= heap[0]
                    heapq.heappop(heap)
                    curr += combind[i][0]
                    heapq.heappush(heap, combind[i][0])
                    multiple = combind[i][1]
        return max(res, multiple * curr)
