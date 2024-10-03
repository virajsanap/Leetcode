class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,
           "V":5,
           "X":10,
           "L":50,
           "C":100,
           "D":500,
           "M":1000}
        out = 0
        l = len(s)
        for i in range(l-1):
            if d[s[i+1]] > d[s[i]]:
                out-=d[s[i]]
            else:
                out+=d[s[i]]
            print(out)
        out+=d[s[l-1]]
        return out
                    
        