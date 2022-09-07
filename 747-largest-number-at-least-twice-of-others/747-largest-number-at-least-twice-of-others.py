class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = second_max_num = max_num_index = -1
        
        for i in range(len(nums)):
            current_num = nums[i]
            if current_num > max_num:
                second_max_num = max_num
                max_num = current_num
                max_num_index = i
            elif current_num > second_max_num:
                second_max_num = current_num
        
        return max_num_index if (max_num >= (2 * second_max_num)) else -1