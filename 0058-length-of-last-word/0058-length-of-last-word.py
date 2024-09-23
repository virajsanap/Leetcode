class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.strip()
        lst=s1.split(" ")
        return len(lst[-1])