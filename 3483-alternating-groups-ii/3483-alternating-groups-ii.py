class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        if k <= 1:
            return len(colors)
        if k > len(colors):
            return 0

        lp = 0
        rp = k
        new_colors = colors * 2
        ans = 0

        def is_valid(arr):
            for i in range(len(arr)-1):
                if arr[i] == arr[i+1]:
                    return False
            return True

        current_valid = is_valid(new_colors[lp:rp])
        if current_valid:
            ans += 1

        lp += 1
        rp += 1

        while lp < len(colors):
            if current_valid:
                if new_colors[rp-1] != new_colors[rp-2]:
                    ans += 1
                    lp += 1
                    rp += 1
                else:
                    current_valid = False
                    lp += 1
                    rp += 1
            
            else:
                # invalid, check entire window
                if is_valid(new_colors[lp:rp]):
                    current_valid = True
                    ans += 1
                lp += 1
                rp += 1

        return ans