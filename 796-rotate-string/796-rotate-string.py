class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        for i in range(len(s)):
            if s[i] == goal[0]:
                start_idx = i
                current_idx = i
                for j in range(len(goal)):
                    if goal[j] != s[current_idx]:
                        break
                    current_idx += 1
                    current_idx %= len(s)
                    if current_idx == start_idx:
                        return True
                
        
        return False