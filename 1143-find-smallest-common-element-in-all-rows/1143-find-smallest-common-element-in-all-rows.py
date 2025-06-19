class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        ref = mat[0]

        for num in ref:
            done = True
            for row in mat[1:]:
                found = False
                left, right = 0, len(row) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if row[mid] == num:
                        found = True
                    if row[mid] < num:
                        left = mid + 1
                    else:
                        right = mid - 1

                if not found:
                    done = False
                    break
            if done:
                return num
        return -1
                
        