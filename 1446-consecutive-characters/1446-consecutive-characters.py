class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        current_streak = max_streak = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 1
        return max_streak