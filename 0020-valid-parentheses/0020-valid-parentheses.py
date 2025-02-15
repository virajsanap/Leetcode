class Solution:
    def isValid(self, s: str) -> bool:
        valid={')':'(',']':'[','}':'{'}
        order = []
        for i in s:
            if i in valid:
                if order and order[-1] == valid[i]:
                    order.pop()
                else:
                    return False
            else:
                order.append(i)
            
        return not order
