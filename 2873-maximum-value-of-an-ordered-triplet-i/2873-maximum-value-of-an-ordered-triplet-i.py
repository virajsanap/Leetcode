class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        i=0
        val = 0
        while i<len(nums)-2:
            j=i+1
            while j<len(nums)-1:
                k=j+1
                while k<len(nums):
                    new_val = (nums[i]-nums[j])*nums[k]
                    val = max(val,new_val)
                    # print(i,j,k)
                    k+=1
                j+=1
            i+=1

        return val if val>0 else 0