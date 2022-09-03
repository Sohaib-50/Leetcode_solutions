class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        last_available_index = 0
        while (last_available_index < len(nums)) and (nums[last_available_index] % 2 == 0):
            last_available_index += 1
        
        if last_available_index == len(nums):
            return nums
        
        for i in range(1, len(nums)):
            if nums[i] % 2 == 0 and last_available_index < i:
                nums[last_available_index], nums[i] = nums[i], nums[last_available_index]
                last_available_index += 1
        
        return nums