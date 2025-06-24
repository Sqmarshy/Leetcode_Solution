class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        dry_day = []
        lakes = {}

        res = [-1 if rains[i] > 0 else 1 for i in range(n)]
        for i in range(n):
            if rains[i] == 0:
                dry_day.append(i)
            else:
                rain_on = rains[i]
                if rain_on in lakes:
                    if len(dry_day) <= 5:
                        found = False
                        for j in range(len(dry_day)):
                            if dry_day[j] > lakes[rain_on]:
                                found = True
                                left = j
                                break
                        if not found: return []
                    else:
                        left, right = 0, len(dry_day) - 1
                        while left < right:
                            mid = (left + right) // 2
                            if dry_day[mid] > lakes[rain_on]:
                                right = mid
                            else:
                                left = mid + 1
                    if dry_day[left] > lakes[rain_on]:
                        lakes[rain_on] = i
                        res[dry_day[left]] = rain_on
                        dry_day.pop(left)
                    else:
                        return []
                else:
                    lakes[rain_on] = i
        return res
