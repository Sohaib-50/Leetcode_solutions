class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = float('-inf')
        current_sum = 0
        for row in accounts:
            for element in row:
                current_sum += element
            max_sum = max(current_sum, max_sum)
            current_sum = 0
            
        return max_sum
