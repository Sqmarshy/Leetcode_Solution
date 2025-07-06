class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.c1 = Counter(nums1)
        self.c2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        curr = self.nums2[index]
        new = curr + val

        self.c2[curr] -= 1
        self.c2[new] += 1
        self.nums2[index] = new

    def count(self, tot: int) -> int:
        res = 0
        for idx, val in self.c1.items():
            diff = tot - idx
            res += self.c2[diff] * self.c1[idx]
        return res

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)