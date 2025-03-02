class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dic = {}

        for nums in nums1:
            dic[nums[0]] = nums[1]

        for nums in nums2:
            dic[nums[0]] = dic.get(nums[0], 0) + nums[1]

        merged_array = []
        for key, value in sorted(dic.items()):
            merged_array.append([key, value])

        return merged_array