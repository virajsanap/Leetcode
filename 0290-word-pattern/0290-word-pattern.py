class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words, w_to_p = s.split(' '), {} 
        if len(pattern)!=len(words): return False
        if len(set(words))!=len(set(pattern)):return False
        
        for i in range(len(words)):
            if words[i] not in w_to_p:
                w_to_p[words[i]]=pattern[i]
            elif w_to_p[words[i]]!=pattern[i]:
                return False
        return True