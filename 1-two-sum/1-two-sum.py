class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            required = target - nums[i]
            if required in indices:
                return i, indices[required]
            indices[nums[i]] = i
            
