class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        ref = mat[0]
        modified = [set(i) for i in mat[1:]]
        for i in ref:
            done = True
            for j in mat:
                if i not in j:
                    done = False
                    break
            if done: return i
        return -1
        