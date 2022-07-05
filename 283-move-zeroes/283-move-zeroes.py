class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_idx = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[last_non_zero_idx] = nums[last_non_zero_idx], nums[i]
                last_non_zero_idx += 1
            
        
