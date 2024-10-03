class Solution:
    def isHappy(self, n: int) -> bool:
        l = len(str(n))
        b=False
        out=0
        for i in str(n):    
            out += int(i)**2
        print(out)
        if out == 1:
            return True
        elif out==2 or out==4:
            return False
        else:
            b =self.isHappy(out)
        return b
            

        
            
        
        