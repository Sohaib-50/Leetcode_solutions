class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            current = nums[i]
            if (target - current) in nums_dict:
                return i, nums_dict[target - current]
                
            nums_dict[current] = i