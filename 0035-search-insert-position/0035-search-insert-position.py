class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        for i in range(l):
            if target<=nums[i]:
                return i
        return l
        