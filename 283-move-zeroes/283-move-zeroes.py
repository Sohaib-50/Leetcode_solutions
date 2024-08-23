class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # find first 0
        for zero_pos in range(len(nums)):
            if nums[zero_pos] == 0:
                break
        # if no 0's
        else:
            return

        for i in range(zero_pos + 1, len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
                zero_pos += 1
        
