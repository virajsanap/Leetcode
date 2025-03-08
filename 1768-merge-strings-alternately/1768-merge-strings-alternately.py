class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        a= len(word1)
        b =len(word2)
        m = max(a,b)
        for i in range(m):
            if i < a:
                res+=word1[i]
            if i < b:
                res+=word2[i]
        print(res)
        return res
        