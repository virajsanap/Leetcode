class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashransom = {}
        hashmag = {}
        for c in magazine:
            hashmag[c] = magazine.count(c)
        print(hashmag)
        for i in ransomNote:
            if i not in hashmag:
                return False
            elif ransomNote.count(i) <= hashmag[i]:
                continue
            else:
                return False
        return True