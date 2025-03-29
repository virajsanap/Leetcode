class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m={}
        for i in nums:
            if i not in m:
                m[i]=1
            else:
                m[i]+=1
        for k, v in m.items():
            if v>1:
                return True
        return False
