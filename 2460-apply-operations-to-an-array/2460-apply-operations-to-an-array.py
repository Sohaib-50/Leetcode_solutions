class Solution:
    def move_zeroes(self, nums: List[int]) -> None:

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
        

    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums) - 1):

            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        self.move_zeroes(nums)

        return nums
