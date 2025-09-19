class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        can = set()
        cannot = set()
        for i in nums:
            if i in cannot:
                continue
            elif i in can:
                cannot.add(i)
                can.remove(i)
            else:
                can.add(i)
        return max(can) if can else -1