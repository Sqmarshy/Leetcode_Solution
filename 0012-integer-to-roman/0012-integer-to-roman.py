class Solution:
    def intToRoman(self, num: int) -> str:
        letter = 'IVXLCDM'
        k = [1, 5, 10, 50, 100, 500, 1000]
        dic = {}
        for i in range(len(letter)):
            dic[k[i]] = letter[i]
        
        res = []
        idx = 1000
        while idx > 0 :
            digit = (num // idx)
            curr = digit * idx
            if not curr: # 0
                idx //= 10
                continue
            num %= idx
            if curr in dic: # 1 5
                res.append(dic[curr])
            elif digit <= 3: # 2 3
                res = res + [dic[idx]] * digit 
            elif digit == 4: # 4
                res.append(dic[idx])
                res.append(dic[idx * 5])
            elif digit == 9: # 9
                res.append(dic[idx])
                res.append(dic[idx * 10])
            else: # 6 7 8
                res.append(dic[idx * 5])
                res = res + [dic[idx]] * (digit - 5)
            idx //= 10
        return ''.join(res)

            

