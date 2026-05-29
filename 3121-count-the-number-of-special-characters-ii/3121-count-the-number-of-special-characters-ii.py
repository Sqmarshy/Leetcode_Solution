class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        res = 0
        dic_upper = {}
        dic_lower = defaultdict(str)
        for i in range(n):
            letter = word[i]
            if ord(letter) <= 90: #Capital letter
                if letter not in dic_upper:
                    dic_upper[letter] = i
            else:
                dic_lower[letter] = i
        
        for letter, position in dic_lower.items():
            capt = letter.upper()
            if capt in dic_upper:
                res += 1 if dic_upper[capt] > position else 0
        
        return res