class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        start = [tops[0], bottoms[0]]
        idx, first_swap_penalty = 0, [0, 1, 1, 0]

        # There can be 2 choice of starting value 
        res = float('inf')
        for val in start:
            # Put start val on top
            curr = 0 + first_swap_penalty[idx]
            for i in range(1, n):
                if tops[i] == val:
                    continue

                if bottoms[i] == val:
                    curr += 1
                else:
                    curr = float('inf')
                    break
            res = min(res, curr)
            idx += 1

            # Put start val at bottom
            curr = 0 + first_swap_penalty[idx]
            for i in range(1, n):
                if bottoms[i] == val:
                    continue
                    
                if tops[i] == val:
                    curr += 1
                else:
                    curr = float('inf')
                    break
            res = min(res, curr)
            idx += 1

        return res if res != float('inf') else -1
