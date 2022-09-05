class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        last_even_index = 0
        last_odd_index = 1
        
        for i in range(len(nums)):
            
            if i % 2 == 1:
                while nums[i] % 2 == 0:
                    nums[i], nums[last_even_index] = nums[last_even_index], nums[i]
                    last_even_index += 2
                
            elif i % 2 == 0:
                while nums[i] % 2 == 1:
                    nums[i], nums[last_odd_index] = nums[last_odd_index], nums[i]
                    last_odd_index += 2
                    
        
        return nums