class Solution:
    def reverse_word(self, s: list, left, right) -> None:
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        
        
    def reverseWords(self, s: str) -> str:
        s = list(s)
        current_word_start = 0
        for i in range(len(s)):
            
            if s[i] != " ":
                continue
            
            self.reverse_word(s, left=current_word_start, right=i-1)
            current_word_start = i + 1
            
        self.reverse_word(s, left=current_word_start, right=i)
        
        return "".join(s)
            
    