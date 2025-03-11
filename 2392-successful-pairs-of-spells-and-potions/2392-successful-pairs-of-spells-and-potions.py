class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        for spell in spells:
            benchmark = success / spell
            left, right = 0, len(potions) - 1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] < benchmark:
                    left = mid + 1
                else:
                    right = mid - 1
            res.append(len(potions) - left)
        return res