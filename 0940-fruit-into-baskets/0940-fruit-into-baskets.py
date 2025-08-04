class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res, left = 0, 0
        count = {}
        for i in range(len(fruits)):
            curr = fruits[i]
            if curr not in count:
                count[curr] = 1
            else:
                count[curr] += 1

            while len(count) > 2:
                c = fruits[left]
                count[c] -= 1
                if count[c] == 0:
                    del count[c]
                left += 1
                
            res = max(res, sum(count.values()))
        return res