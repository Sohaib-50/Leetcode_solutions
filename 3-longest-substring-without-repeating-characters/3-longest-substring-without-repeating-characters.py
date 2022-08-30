class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        
        max_len_sofar = 1
        window_chars = set()
        window_chars.add(s[0])
        start = 0
        
        for end in range(1, len(s)):
            if s[end] in window_chars:  # need to stop sliding open window here

                max_len_sofar = max((end - start), max_len_sofar)  # update max length if length of latest window is the highest so far
                
                # adjust window size
                while (s[start] != s[end]) and start < end:
                    window_chars.remove(s[start])  # remove character from window
                    start += 1  # make window smaller by moving window start ahead
                
                if s[start] == s[end] and start < end:
                    window_chars.remove(s[start])  # remove character from window
                    start += 1  # make window smaller by moving window start ahead
            
            window_chars.add(s[end])
        
        return max((end - start) + 1, max_len_sofar)
                

                    