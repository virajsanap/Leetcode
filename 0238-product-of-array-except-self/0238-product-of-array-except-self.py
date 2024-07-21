class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        l = len(nums)
        prodlist = [1]*l
        prefix_prod = 1
        postfix_prod = 1
        for i in range(l):
            prodlist[i] *= prefix_prod
            prefix_prod =prefix_prod*nums[i]
            
            prodlist[l-i-1] *= postfix_prod
            postfix_prod *= nums[l-i-1]
            
        return prodlist
        
