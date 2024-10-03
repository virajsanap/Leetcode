class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a = "".join(c for c in s if c.isalnum())
        ls = list[s]
        rs = a[::-1]
        print(a)
        print(rs)
        if rs == a:
            return True
        return False
        