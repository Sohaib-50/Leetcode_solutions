class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {nums[j]: j for j in range(len(nums))}
        
        for i in range(len(nums)):
            required = target - nums[i]
            if required in indices and i != indices[required]:
                return (i, indices[target - nums[i]])
