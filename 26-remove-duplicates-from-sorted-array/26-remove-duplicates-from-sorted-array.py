class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums)) == 1:
            return 1
        
        available_idx = 1
        
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[available_idx] = nums[i]
                available_idx += 1
        
        return available_idx
                