class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = float("-inf")
        container_start = 0
        container_end = len(height) - 1
        while (container_start < container_end):
            area = (container_end - container_start)\
                * min(height[container_start], height[container_end]) 
            max_area = max(max_area, area)

            if height[container_start] < height[container_end]:
                container_start += 1
            else:
                container_end -= 1

        return max_area
