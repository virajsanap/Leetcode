class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        for i in range(len(self.nums)):
            for j in range(i+1,len(self.nums)):
                if nums[j]==self.target - nums[i]:
                    return [i,j]