class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits=""
        for i in digits:     
            str_digits+=str(i)
        added_str = str(int(str_digits)+1)
        res=[]
        for i in added_str:
            res.append(int(i))
        return res