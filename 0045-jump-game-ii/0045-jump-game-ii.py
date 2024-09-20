class Solution:
    def jump(self, nums: List[int]) -> int:
        last,current, nxt, count, i = len(nums)-1,-1,0,0,0
        while nxt <last:
            if i > current:
                count+=1
                current = nxt
            nxt = max(nxt, nums[i]+i)
            i+=1
        return count
            
                
                
            
            