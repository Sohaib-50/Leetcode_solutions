class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index_to_mark = abs(nums[i]) - 1
            nums[index_to_mark] = -(abs(nums[index_to_mark]))

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
