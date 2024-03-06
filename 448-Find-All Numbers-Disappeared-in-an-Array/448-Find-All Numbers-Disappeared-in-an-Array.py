class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        all_nums = set(range(1, len(nums) + 1))
        for i in nums:
            if i in all_nums:
                all_nums.remove(i)
        return list(all_nums)
