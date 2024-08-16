class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = ['a','e','i','o','u']
        left =0 
        max_vowel_count = vowel_count = sum(c in vow for c in s[:k])
        for right in range(k, len(s)):
            vowel_count += s[right] in vow
            vowel_count -= s[left] in vow
            left +=1
            max_vowel_count = max(max_vowel_count,vowel_count)
        return max_vowel_count
            