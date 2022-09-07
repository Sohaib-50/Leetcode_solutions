class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num_index = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[max_num_index]:
                max_num_index = i
        
        for i in range(len(nums)):
            if (nums[max_num_index] < (2 * nums[i])) and (i != max_num_index):
                return -1
        
        return max_num_index