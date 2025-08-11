class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = str(n)
        combi = itertools.permutations(str(n))
        # def backtrack(curr, idx):
        #     if curr and curr[0] == '0':
        #         return
        #     if len(curr) == len(s):
        #         combi.add(int(''.join(curr)))
        #         return
        #     for i in range(0, len(s)):
        #         if i in idx:
        #             continue
        #         new = idx.copy()
        #         new.add(i)
        #         backtrack(curr + [s[i]], new)

        # backtrack([], set())
        for i in combi:
            if i[0] != '0' and bin(int("".join(i))).count('1') == 1:
                return True
        return False