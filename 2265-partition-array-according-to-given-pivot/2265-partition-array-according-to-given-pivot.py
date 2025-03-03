class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        count = 0
        smaller, greater = [], []
        for i in nums:
            if i < pivot:
                smaller.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                count += 1
        
        return smaller + [pivot] * count + greater