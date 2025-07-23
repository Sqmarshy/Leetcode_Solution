class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        stack2 = []
        score = 0
        higher, lower = '', ''
        
        if x >= y:
            higher, lower = 'ab', 'ba'
        else:
            higher, lower = 'ba', 'ab'

        for i in s:
            if not stack:
                stack.append(i)
            else:
                if stack[-1] + i == higher:
                    score += max(x, y)
                    stack.pop()
                else:
                    stack.append(i)

        for i in stack:
            if not stack2:
                stack2.append(i)
            else:
                if stack2[-1] + i == lower:
                    score += min(x, y)
                    stack2.pop()
                else:
                    stack2.append(i)
                    
        return score