class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i +1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return (i, j)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i, j
        
        
#     nums_dict = {}
#         for i in range(len(nums)):
#             current_number = nums[i]
#             nums_dict[current_number] = i
            
#         for i in range(len(nums)):
#             current_number = nums[i]
#             if (target - current_number) in nums_dict:
#                 return i, nums_dict[target - current_number]
        
        
#         nums_dict = {}
#         for i in range(len(nums)):
#             current = nums[i]
#             if (target - current) in nums_dict:
#                 return i, nums_dict[target - current]
                
#             nums_dict[current] = i