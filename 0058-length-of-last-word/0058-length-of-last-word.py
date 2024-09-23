class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.strip()
        lst=s1.split(" ")
        print(lst)
        return len(lst[-1])