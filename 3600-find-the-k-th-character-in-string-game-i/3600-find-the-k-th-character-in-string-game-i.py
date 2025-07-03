class Solution:
    def kthCharacter(self, k: int) -> str:
        s = 'a'
        while len(s) < k:
            new = []
            for i in s:
                chara = chr((ord(i) - ord('a') + 1) % 26 + ord('a'))
                new.append(chara)
            s = s + ''.join(new)
        return s[k - 1]