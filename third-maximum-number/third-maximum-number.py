class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = second_max = third_max = float("-inf")
        for i in nums:
            if (i == first_max) or (i == second_max) or (i == third_max):
                continue
                
            if i > first_max:
                third_max = second_max
                second_max = first_max
                first_max = i
            elif i > second_max:
                third_max = second_max
                second_max = i
            elif i > third_max:
                third_max = i
        
        return third_max if third_max != float("-inf") else first_max