class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        found={}
        for i, num in enumerate(nums):
            if num in found and i-found[num]<=k:
                return True
            found[num]=i
        return False
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if nums[i]==nums[j] and abs(j-i)<=k and i!=j:
        #             print([i,j])
        #             return True
        # return False
        
        