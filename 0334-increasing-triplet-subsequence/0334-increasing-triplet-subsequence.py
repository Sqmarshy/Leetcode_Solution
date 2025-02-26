class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')
        for i in nums:
            if i < first and i < second:
                first = i
            elif i > first and i < second:
                second = i
            elif i > first and i > second:
                return True
        return False