class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count_zeroes = 0
        start = end = 0
        result = 0

        while end < len(nums):
            
            if nums[end] == 0:
                count_zeroes += 1

            while count_zeroes > 1:
                if nums[start] == 0:
                    count_zeroes -= 1
                start += 1
            
            result = max(result, end - start + 1)

            end += 1

        return result - 1
