class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        a1, b1 = blue, red
        a2, b2 = red, blue
        first = [a1, b1]
        second = [a2, b2]

        res = 0
        curr1 = 0
        for i in range(1, red + blue + 1):
            if first[curr1] >= i:
                first[curr1] -= i
                curr1 = (curr1 + 1) % 2
            else:
                break
        res = max(res, i - 1)

        curr2 = 0
        for j in range(1, red + blue + 1):
            if second[curr2] >= j:
                second[curr2] -= j
                curr2 = (curr2 + 1) % 2
            else:
                break
        return max(res, j - 1)