class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0
        for f in range(len(nums)):
            if nums[f]!=0 and nums[s]==0:
                nums[f],nums[s]=nums[s],nums[f]
            if nums[s]!=0:
                s+=1
        print(nums)
        