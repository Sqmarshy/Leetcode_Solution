class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        rows = len(score)
        k_score = [(score[i][k], i) for i in range(rows)]
        k_score.sort(reverse = True)
        res = []
        for s, idx in k_score:
            res.append(score[idx])
        return res