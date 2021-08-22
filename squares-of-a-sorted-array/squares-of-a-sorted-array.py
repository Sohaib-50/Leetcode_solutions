class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_squares_arr = [0 for num in nums]
        
        left = 0
        right = i = (len(nums) - 1)
        
        while i >= 0:
            if abs(nums[left]) > abs(nums[right]):
                sorted_squares_arr[i] = nums[left] ** 2
                left += 1
            else:
                sorted_squares_arr[i] = nums[right] ** 2
                right -= 1
            i -= 1
        
        return sorted_squares_arr