class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = float('inf')
        curr = 0
        left = 0
        for i in range(len(blocks)):
            if i - left + 1 < k:
                if blocks[i] == 'W':
                    curr += 1
                continue
            curr = curr + 1 if blocks[i] == 'W' else curr
            res = res if res < curr else curr
            curr = curr - 1 if blocks[left] == 'W' else curr
            left += 1
        return res 