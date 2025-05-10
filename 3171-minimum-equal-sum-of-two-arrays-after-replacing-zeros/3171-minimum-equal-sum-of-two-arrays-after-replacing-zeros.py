class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        z1, z2 = nums1.count(0), nums2.count(0)
        min_s1, min_s2 = s1 + z1, s2 + z2
        if z1 == z2 == 0:
            return s1 if s1 == s2 else -1
        elif z1 == 0 or z2 == 0:
            if z1 == 0:
                return s1 if min_s2 <= s1 else -1
            else:
                return s2 if min_s1 <= s2 else -1
        else:
            return max(min_s1, min_s2)