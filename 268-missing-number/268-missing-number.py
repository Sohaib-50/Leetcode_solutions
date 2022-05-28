class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if sorted_nums[i] != i:
                return i
        return i + 1