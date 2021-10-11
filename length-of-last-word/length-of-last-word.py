class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        current_word_len = 0
        space_encountered = False
        
        for char in s:
            if char == " ":
                space_encountered = True
            else:
                if space_encountered:
                    current_word_len = 1
                    space_encountered = False
                else:
                    current_word_len += 1
                    
        return current_word_len