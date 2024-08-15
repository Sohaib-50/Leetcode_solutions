class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        new_valid_pos = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[new_valid_pos] = nums[i]
                new_valid_pos += 1
        return new_valid_pos
