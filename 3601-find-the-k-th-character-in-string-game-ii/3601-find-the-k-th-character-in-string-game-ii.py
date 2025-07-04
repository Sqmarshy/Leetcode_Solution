class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        num = 0
        while 2 ** num < k:
            num += 1
        
        shift = 0
        idx = num - 1
        while num:
            idx = num - 1
            curr = operations[idx]
            array_length = 2 ** num
            # K first half
            if k <= array_length // 2:
                pass
            # K second half
            else:
                k -= array_length // 2
                shift += 1 if curr == 1 else 0
            num -= 1
        
        return chr(ord('a') + (shift % 26))

        return num