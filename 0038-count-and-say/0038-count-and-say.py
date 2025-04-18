class Solution:
    def recurr(self, nums, k, n):
        res = ''
        stack = []
        for i in nums:
            if not stack:
                stack.append(i)
            else:
                if i == stack[-1]:
                    stack.append(i)
                else:
                    res += str(len(stack)) + stack[-1]
                    stack = [i]
        if stack:
            res += str(len(stack)) + stack[0]
        return res if k == n else self.recurr(res,k + 1,n)

    def countAndSay(self, n: int) -> str:
        return self.recurr('1', 2, n) if n != 1 else '1'