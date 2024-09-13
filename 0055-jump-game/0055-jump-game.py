class Solution:
    def canJump(self, nums: List[int]) -> bool:
        e = 0
        for n in nums:
            if e<0:
                return False
            elif n>e:
                e=n    
            e-=1
        return True
            