class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_count_s = {}
        for char in s:
            if char in chars_count_s:
                chars_count_s[char] += 1
            else:
                chars_count_s[char] = 1
        
        chars_count_t = {}
        for char in t:
            if char in chars_count_t:
                chars_count_t[char] += 1
            else:
                chars_count_t[char] = 1
                
        return chars_count_s == chars_count_t