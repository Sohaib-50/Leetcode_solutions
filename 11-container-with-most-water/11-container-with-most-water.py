class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_sofar = 0
        l = 0
        r = len(height) - 1
        while l < r:
            l_height = height[l]
            r_height = height[r]
            max_sofar = max(max_sofar, (min(l_height, r_height) * (r - l)))
            if l_height < r_height:
                l += 1
            else:
                r -= 1
        return max_sofar