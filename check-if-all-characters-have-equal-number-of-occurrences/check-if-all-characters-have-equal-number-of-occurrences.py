class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        
        x = counts[s[0]]
        for char in s:
            if counts[char] != x:
                return False
            
        return True