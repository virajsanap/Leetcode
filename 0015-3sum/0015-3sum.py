class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        out =[]
        nums = sorted(nums)
        for i in range(l):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            j =i+1
            k=l-1
            while j<k:
                if nums[i]+nums[j]+nums[k]>0:
                    k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    out.append([nums[i],nums[j],nums[k]])
                    j+=1
                    
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
        return out
       
                    
        
            
        