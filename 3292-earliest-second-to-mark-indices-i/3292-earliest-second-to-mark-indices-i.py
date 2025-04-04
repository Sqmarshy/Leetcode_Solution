class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        left = 0
        right = len(changeIndices) - 1

        def is_valid(second):
            idxs = {}
            for i in range(second - 1, -1, -1):
                curr = changeIndices[i]
                if curr not in idxs:
                    idxs[curr] = i
                if len(idxs) == len(nums):
                    break
            if len(idxs) != len(nums):
                return False

            # Modifying the initial implementation
            move = 0
            for idx, pos in reversed(list(idxs.items())):
                move += nums[idx-1] + 1
                if pos + 1 < move or move > second:
                    return False
            return True

        # Binary Search
        while left <= right:
            mid = (left+right) // 2
            if is_valid(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left if is_valid(left) else -1