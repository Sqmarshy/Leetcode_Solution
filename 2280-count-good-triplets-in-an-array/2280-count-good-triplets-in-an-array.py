class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos1 = {nums1[i]: i for i in range(n)} # map val : idx in nums1
        mapped_nums2 = [pos1[num] for num in nums2] # map num2 val to num1 idx
        left_smaller = SortedList() 
        
        res = 0
        for i in range(n):
            curr_pos = mapped_nums2[i]          
            left_count = left_smaller.bisect_right(curr_pos)         
            right_count = (n - curr_pos - 1) - (i - left_count)         
            res += left_count * right_count         
            left_smaller.add(curr_pos)
        return res