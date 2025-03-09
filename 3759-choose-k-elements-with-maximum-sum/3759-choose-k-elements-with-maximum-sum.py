class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        res = [0] * len(nums1)
        nums1 = [(nums1[i], i) for i in range(len(nums1))]
        nums1.sort()
        heap = []
        left = 0
        running_sum = 0
        for i in range(len(nums1)):
            val, idx = nums1[i]
            while nums1[left][0] < val:
                curr = nums2[nums1[left][1]]
                if len(heap) >= k:
                    if curr > heap[0]:
                        running_sum -= heap[0]
                        heapq.heappop(heap)

                        running_sum += curr
                        heapq.heappush(heap, curr)
                else:
                    running_sum += curr
                    heapq.heappush(heap, curr)
                left += 1
            res[idx] = running_sum
        return res
                