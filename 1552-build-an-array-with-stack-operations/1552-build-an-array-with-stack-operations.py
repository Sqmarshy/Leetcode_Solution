class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        tar = 0
        curr = 1
        while tar < len(target):
            if target[tar] == curr:
                res.append("Push")
                tar += 1
                curr += 1
            else:
                curr += 1
                res.append("Push")
                res.append("Pop")
        return res
