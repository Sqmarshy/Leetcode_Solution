class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for letter in s:
            if not stack:
                stack.append(letter)
            else:
                curr = ord(letter) - ord('a')
                prev = ord(stack[-1]) - ord('a')
                if (curr in (0, 25) and prev in (0, 25)) and curr != prev:
                    stack.pop()
                elif abs(curr - prev) == 1:
                    stack.pop()
                else:
                    stack.append(letter)
        return ''.join(stack)