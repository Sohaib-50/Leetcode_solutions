class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        free_pos = 0

        for num in nums:
          
            # if first 2 positions or the number 2 positions behind is different, copy current number to free_pos
            if free_pos <= 1 or (nums[free_pos - 2] != num):
                nums[free_pos] = num
                free_pos += 1

        return free_pos
