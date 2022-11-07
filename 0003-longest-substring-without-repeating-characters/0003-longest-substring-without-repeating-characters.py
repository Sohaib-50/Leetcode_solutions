class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        start = 0
        current_window_size = 0
        max_window_size = 1
        current_window_chars = {s[0]}
        
        for end in range(1, len(s)):
            current_char = s[end]
            if current_char in current_window_chars:
                while s[start] != current_char:
                    current_window_chars.remove(s[start])
                    start += 1
                start += 1
                
            current_window_chars.add(s[end])
            max_window_size = max(max_window_size, len(current_window_chars))
            
            
            
        return max_window_size