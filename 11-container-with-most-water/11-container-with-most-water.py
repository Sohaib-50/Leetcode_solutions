class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_sofar = float('-inf')
        l = 0 
        r = len(height) - 1
        while l < r:
            max_sofar = max(max_sofar, 
                (r - l) * min(height[r], height[l])
            )
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_sofar
