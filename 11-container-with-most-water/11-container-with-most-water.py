class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # attempt 1: brute force try all possible containers- fails due to Time Limit Exceeded
        # max_area = 0
        # for i in range(len(height) - 1):
        #     for j in range(i + 1, len(height)):
        #         max_area = max(
        #             max_area,
        #             (j - i) * min(height[i], height[j])
        #         )
        # return max_area

        # attempt 2: Start with widest container, move inwards by moving from side of shorter height
        # Intuition: max area = max height * max width
        max_area = 0
        l = 0
        r = len(height) - 1

        while l < r:
            max_area = max(
                max_area,
                (r - l) * min(height[r], height[l])
            )
        
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            
        return max_area
