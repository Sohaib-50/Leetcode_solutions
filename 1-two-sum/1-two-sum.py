class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_map = {nums[j]: j for j in range(len(nums))}
        
        for i in range(len(nums)):
            required = target - nums[i]
            if required in indices_map and i != indices_map[required]:
                return (i, indices_map[target - nums[i]])
