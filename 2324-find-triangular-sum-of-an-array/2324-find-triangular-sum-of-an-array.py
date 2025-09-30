class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        temp = nums.copy()
        while len(temp) > 1:
            curr = []
            for i in range(len(temp) - 1):
                curr.append((temp[i] + temp[i + 1]) % 10)
            temp = curr.copy()
        return temp[0]