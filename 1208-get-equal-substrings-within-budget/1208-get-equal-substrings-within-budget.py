class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ## Thought process:
        # looks like a sliding window problem clearly. The window can expand till its elements satisfy the condition of maxCost limit
        # we can expand window automatically
        # Then check if cost is exceeded, so start shrinking from left till cost threshold is satisfied.

        ans = 0
        window_start = 0
        window_cost = 0

        for window_end in range(len(s)):

            window_cost += abs(ord(s[window_end]) - ord(t[window_end]))
            
            while window_cost > maxCost:
                window_cost -=  abs(ord(s[window_start]) - ord(t[window_start]))
                window_start += 1

            ans = max(ans, (window_end - window_start) + 1)

        return ans
