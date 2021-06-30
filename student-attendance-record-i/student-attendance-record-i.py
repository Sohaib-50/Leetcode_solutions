class Solution:
    def checkRecord(self, s: str) -> bool:
        
        count_A = count_consecutive_L = 0
        i = 0
        while (count_A < 2) and (count_consecutive_L < 3) and (i < len(s)):
            if s[i] == "L":
                count_consecutive_L += 1
            else:
                if s[i] == "A":
                    count_A += 1
                count_consecutive_L = 0
            i += 1
        
        return count_A < 2 and count_consecutive_L < 3