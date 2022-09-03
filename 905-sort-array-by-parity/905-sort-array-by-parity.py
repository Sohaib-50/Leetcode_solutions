class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Quick Sort Approach
        
        low = 0
        high = len(nums) -1
        
        while low < high:
            if (nums[low] % 2 == 1) and (nums[high] % 2 == 0):
                nums[low], nums[high] = nums[high], nums[low]
                
            if nums[low] % 2 == 0:
                low += 1
            
            if nums[high] % 2 == 1:
                high -= 1
        
        return nums
            
            