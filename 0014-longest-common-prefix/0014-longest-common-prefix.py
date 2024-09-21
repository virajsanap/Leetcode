class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        print(shortest)
        for i,v in enumerate(shortest):
            print(i, v)
            for s in strs:
                if s[i]!=v:
                    return shortest[:i]
        return shortest
                