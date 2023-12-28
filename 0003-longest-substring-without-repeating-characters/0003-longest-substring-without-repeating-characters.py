class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        current_window_chars = set()
        ans = 0
        for end in range(len(s)):
            char = s[end]
            if char in current_window_chars:
                while s[start] != char:
                    current_window_chars.remove(s[start])
                    start += 1
                start += 1

            else:
                current_window_chars.add(char)

            
            ans = max(ans, end - start + 1)
            print(end, s[start:end + 1], ans, current_window_chars)

        return ans

        
