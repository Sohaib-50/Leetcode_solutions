class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        def water_amount(i, j):
            w = abs(i - j)
            h = min(height[i], height[j])
            return w * h
        
        left, right = 0, len(height) - 1
        max_sofar = float('-inf')
        while left < right:
            max_sofar = max(max_sofar, water_amount(left, right))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_sofar