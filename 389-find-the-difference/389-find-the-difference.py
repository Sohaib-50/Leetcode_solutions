class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = 0
        
        for char in s:
            x ^= ord(char)
        
        for char in t:
            x ^= ord(char)
            
        return chr(x)