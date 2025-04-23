class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # find first 0
        for i, num in enumerate(nums):
            if num == 0:
                break
        
        zero_ptr = i
        for i in range(zero_ptr + 1, len(nums)):
            print(i, nums[i])
            if nums[i] != 0:
                nums[zero_ptr], nums[i] = nums[i], nums[zero_ptr]
                
                for j in range(zero_ptr + 1, i):
                    if nums[j] == 0:
                        zero_ptr = j
                        break
                else:
                    zero_ptr = i
            
