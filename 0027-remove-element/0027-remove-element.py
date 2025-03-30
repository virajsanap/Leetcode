class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        k=0
        while i<len(nums)-1:
            for j in range(i+1,len(nums)):
                # print(i,j)
                if nums[i]==val and nums[j]!=val:
                    temp=nums[j]
                    nums[j]=nums[i]
                    nums[i]=temp
                    break
            i+=1
            j+=1
        res=0
        for i in nums:
            if i!=val:
                res+=1
            
        return res
        


        
