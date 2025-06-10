class Solution:
    def maxDifference(self, s: str) -> int:
        maxi_odd, mini_even = 0, 9999999
        count = Counter(s)
        for key, val in count.items():
            if val % 2 == 0:
                mini_even = min(mini_even, val)
            else:
                maxi_odd = max(maxi_odd, val)
        
        return maxi_odd - mini_even