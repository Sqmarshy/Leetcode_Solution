class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n, idx = len(bits), 0
        while idx < n:
            if bits[idx] == 0:
                if idx == n - 1:
                    return True
                idx += 1
            else:
                idx += 2
        return False
                