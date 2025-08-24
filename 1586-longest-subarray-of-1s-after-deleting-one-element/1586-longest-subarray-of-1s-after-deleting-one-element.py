class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if nums[0] == 1 and len(set(nums)) == 1:
            return len(nums) - 1
        nums.append('x')
        stack = []
        res = []
        for i in nums:
            if not stack:
                stack.append(i)
            else:
                if stack[-1] != i:
                    if stack[-1] == 1:
                        res.append(len(stack))
                        stack = []
                        stack.append(i)
                    else:
                        if len(stack) > 1:
                            res.append('no')
                        else:
                            res.append('yes')
                        stack = []
                        stack.append(i)
                else:
                    stack.append(i)
        highest = 0
        for i in range(len(res)):
            if type(res[i]) == int:
                highest = max(highest,res[i])
            else:
                if i == 0:
                    if res[i] == 'yes':
                        if len(res) >= 2:
                            hgihest = max(highest, res[1])
                elif i == len(res) - 1:
                    if res[i] == 'yes':
                        highest = max(highest,res[len(res)-2])
                else:
                    if res[i] == 'yes':
                        highest = max(highest, res[i-1]+res[i+1])
        return highest
