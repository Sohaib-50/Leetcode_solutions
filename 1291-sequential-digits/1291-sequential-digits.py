class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def helper(low, high, current, ans):
            last_digit = current % 10
            if last_digit + 1 > 9:  # base case 1 
                return
            current = (current * 10) + (last_digit + 1)  # append new digit
            if current in range(low, high + 1):
                ans.append(current)
            elif current > high:  # base case 2
                return
            
            helper(low, high, current, ans)  # recursive call
            
        ans = []
        for i in range(1, 9):
            helper(low, high, i, ans)
            
        return sorted(ans)

        
        