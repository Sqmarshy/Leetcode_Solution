class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        left, res = 0, 0
        n = len(colors)

        # # First intuition
        # colors_extended = colors + colors
        # for i in range(1, len(colors_extended)):
        #     if left >= n:
        #         return res
        #     if colors_extended[i] == colors_extended[i - 1]:
        #         left = i
        #     if i - left + 1 < k:
        #         continue
        #     res += 1
        #     left += 1
        # return res

        # Space Optimized 
        ending_point = n + k - 1 # If last element of colors (color[n-1]) is the start of subarray, this will be the ending point of that subarray
        for i in range(1, ending_point):
            if colors[i % n] == colors[(i - 1) % n]:
                left = i
            if i - left + 1 < k:
                continue
            res += 1
            left += 1
        return res
