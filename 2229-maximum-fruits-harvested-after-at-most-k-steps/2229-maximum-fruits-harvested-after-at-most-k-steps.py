class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        count = {i[0]:i[1] for i in fruits}
        pos_fruit = {startPos:0}
        left, right = startPos - k, startPos + k
        curr_left, curr_right = 0, 0
        res = 0

        for i in range(startPos - 1, left - 1, -1):
            if i in count:
                curr_left += count[i]
            pos_fruit[i] = curr_left
        
        for i in range(startPos + 1, right + 1):
            if i in count:
                curr_right += count[i]
            pos_fruit[i] = curr_right
        
        left_w, right_w = left, startPos
        while left_w < startPos:
            res = max(res, pos_fruit[left_w] + pos_fruit[right_w])
            left_w += 2
            right_w += 1

        right_w, left_w = right, startPos
        while right_w > startPos:
            res = max(res, pos_fruit[left_w] + pos_fruit[right_w])
            right_w -= 2
            left_w -= 1

        if startPos in count:
            res += count[startPos]
        return res