class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        
        for i in range(len(nums) - 2):
            # to avoid duplicates
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
                
            target = -nums[i]
            low = i + 1
            high = len(nums) -1
            
            while low < high:
                if (nums[low] + nums[high]) == target:
                    ans.append([nums[i], nums[low], nums[high]])
                    
                    # to avoid duplicates
                    while (low < high) and (nums[low] == nums[low + 1]):
                        low += 1
                    while (low < high) and (nums[high] == nums[high - 1]):
                        high -= 1
                    
                    low += 1
                    high -=1
                    
                elif (nums[low] + nums[high]) < target:
                    low += 1
                
                else:
                    high -= 1
                    
        return ans
        
        
#         ans = []
#         used = set()
#         for i in nums:
#             if i in used:
#                 continue
#             used.add(i)
#             j, k = self.twoSum(nums, -i)
#             if j == k == None:
#                 continue
#             ans.append([i, j, k])
#         return ans
        
        
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_set = set(nums)

#         for j in nums_set:
#             required = target - j
#             if required in nums_set and len(set((-target, j, required))) == 3:
#                 return j, required
#         return [None, None]
    
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         for k in range(len(nums)):
#             i, j = self.twoSum(nums, -nums[k], k)
#             if i == j == -1:
#                 continue
#             ans.append([nums[i], nums[j], nums[k]])
#         return ans
            
                
        
        
#     def twoSum(self, nums: List[int], target: int, exclude_index: int) -> List[int]:
#         indices = {nums[j]: j for j in range(len(nums))}
        
#         for i in range(exclude_index + 1, len(nums)):
#             required = target - nums[i]
#             if required in indices and i != indices[required] and indices[required] != exclude_index:
#                 return (i, indices[target - nums[i]])
        
#         return (-1, -1)
        