class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def x_sum(start, end):
            array = nums[start:end+1]
            if len(set(array)) < x:
                return sum(array)
            else:
                count = Counter(array)
                heap = []
                for key, value in count.items():
                    to_heap = (value, key)
                    heapq.heappush(heap, to_heap)
                    if len(heap) > x:
                        heapq.heappop(heap)
                sums = 0
                for i in heap:
                    sums += i[0] * i[1]
                return sums

        n = len(nums)
        res = []
        for i in range(0,n - k + 1):
            num = x_sum(i,i+k-1)
            res.append(num)
        return res
