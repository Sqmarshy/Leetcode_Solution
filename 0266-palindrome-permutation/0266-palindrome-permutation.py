class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        odd = False
        for _, val in count.items():
            if odd and val % 2 == 1:
                return False
            elif val % 2 == 1:
                odd = True
        return True