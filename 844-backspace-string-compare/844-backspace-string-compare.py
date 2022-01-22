class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        final_s = []
        final_t = []
        
        for char in s:
            if char != "#":
                final_s.append(char)
            elif len(final_s) > 0:
                final_s.pop()
                
        for char in t:
            if char != "#":
                final_t.append(char)
            elif len(final_t) > 0:
                final_t.pop()
    
        return final_t == final_s