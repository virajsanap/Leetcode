class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pairs = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (i*j)%k==0 and nums[i]==nums[j]:
                    pairs+=1
        return pairs