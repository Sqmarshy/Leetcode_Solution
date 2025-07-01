class Solution:
    def possibleStringCount(self, word: str) -> int:
        stack = []
        res = 1
        for i in word:
            if not stack:
                stack.append(i)
            else:
                if stack[-1] == i:
                    stack.append(i)
                else:
                    res += len(stack) - 1
                    stack = [i]
        return res + len(stack)  -1