class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # Base Case
        if numFriends == 1:
            return word
        
        # SLiding window starting with lex highest chara
        largest = max(word, key = lambda x: ord(x))
        max_length = len(word) - (numFriends - 1)
        res = largest
        for i in range(len(word)):
            if word[i] == largest:
                right = min(i + max_length, len(word))
                res = max(res, word[i:right])
        return res
