class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = {"red": 0,
            "white": 0,
            "blue": 0}
        for color in nums:
            if color == 0:
                colors["red"] += 1
            elif color == 1:
                colors["white"] += 1
            else:
                colors["blue"] += 1
                
            
        i = 0
        for j in range(colors["red"]):
            nums[i] = 0
            i += 1
            
        for j in range(colors["white"]):
            nums[i] = 1
            i += 1
            
        for j in range(colors["blue"]):
            nums[i] = 2
            i += 1
        