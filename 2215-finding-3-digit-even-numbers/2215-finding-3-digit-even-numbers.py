class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = {i:0 for i in range(10)}
        for i in digits:
            if count[i] < 3:
                count[i] += 1
        
        nums = []
        for i in count:
            while count[i]:
                nums.append(i)
                count[i] -= 1
        
        res = set()
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                continue
            a = nums[i] * 100

            for j in range(n):
                if j == i:
                    continue
                b = nums[j] * 10

                for k in range(n):
                    if k == i or k == j or nums[k] % 2 != 0 :
                        continue
                    res.add(a + b + nums[k])

        return sorted(res)