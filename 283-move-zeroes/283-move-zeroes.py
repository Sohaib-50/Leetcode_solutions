class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_nonzero_ptr = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                next_nonzero_ptr = i
                break

        if next_nonzero_ptr == -1 or next_nonzero_ptr == len(nums) - 1:
            return

        i = next_nonzero_ptr + 1
        while i < len(nums):

            if nums[i] != 0:
                # swap
                nums[next_nonzero_ptr] = nums[i]
                nums[i] = 0 
                next_nonzero_ptr += 1
            i += 1

        return
