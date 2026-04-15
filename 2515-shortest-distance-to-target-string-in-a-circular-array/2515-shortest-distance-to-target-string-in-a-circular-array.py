class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        dic = defaultdict(list)
        for idx, word in enumerate(words):
            dic[word].append(idx)
        
        if len(dic[target]) == 0:
            return -1
        else:
            res = 999999999
            for t in dic[target]:
                right = abs(startIndex - t)
                left = len(words) - right
                res = min(left, right, res)
        return res