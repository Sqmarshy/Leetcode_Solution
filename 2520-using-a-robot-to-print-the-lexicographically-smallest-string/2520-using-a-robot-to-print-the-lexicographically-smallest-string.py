class Solution:
    def robotWithString(self, s: str) -> str:
        minimum = [''] * len(s)
        mini = 'z'
        for i in range(len(s) - 1, -1, -1):
            mini = min(mini, s[i])
            minimum[i] = mini

        res = []
        stack = []
        for idx in range(len(s)):
            # Track past letters
            while stack and stack[-1] <= minimum[idx]:
                res.append(stack.pop())

            # Deal with current letter
            curr = s[idx]
            if curr <= minimum[idx]:
                res.append(curr)
            else:
                stack.append(curr)

        return ''.join(res + stack[::-1])
