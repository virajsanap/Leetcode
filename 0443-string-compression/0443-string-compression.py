class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0 
        res = 0 
        while i < len(chars):
            groupLength = 1
            while (i+groupLength<len(chars) and chars[i+groupLength] == chars[i]):
                groupLength += 1
                
            chars[res] = chars[i]
            res += 1
            
            if groupLength>1 :
                str_repr = str(groupLength)
                chars[res:res+len(str_repr)] = list(str_repr)
                res+=len(str_repr)
            
            i+=groupLength
        return res
            
            
            