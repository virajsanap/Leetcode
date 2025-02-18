class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls=len(s)
        lt=len(t)

        if ls!=lt:
            return False
        
        hs={}
        ht={}

        for i in s:
            if i in hs:
                hs[i]+=1
            else:
                hs[i]=1
        print(hs)  
        for j in t:
            if j in ht:
                ht[j]+=1
            else:
                ht[j]=1
        print(ht)  
        
        if hs==ht:
            return True
        return False