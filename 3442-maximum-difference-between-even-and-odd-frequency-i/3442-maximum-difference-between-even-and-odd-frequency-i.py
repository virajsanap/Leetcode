class Solution:
    def maxDifference(self, s: str) -> int:
        m={}
        for i in s:
            m[i]=1+m.get(i,0)
        
        a1=-inf
        a2=inf
        for i in m.values():
            if i%2==0:
                a2=min(a2,i)
            else:
                a1=max(a1,i)
        print(a1,a2)
        
        return a1-a2
