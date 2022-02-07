class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        charmap = [0 for _ in range(26)]
        
        for char in t:
            charmap[ord(char) - ord("a")] += 1
        
        for char in s:
            charmap[ord(char) - ord("a")] -= 1
        
        for i in range(len(charmap)):
            if charmap[i] == 1:
                return chr(i + 97)
        
            