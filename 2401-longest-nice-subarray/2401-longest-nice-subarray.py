class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ## Idea:
        # - if in binary rep, two numbers don't have 1 at any same place, their AND will be 0.
        # - eg:
        #  - 1100, 1000 -> 1000 (have 1 at 4th place)
        #  - 1100, 0011 -> 0000 (don't have 1 at any same place)
        # - We can keep track on which 1 positions have been used up. If a new number has 1 in that position, then it cant be part of that nice subarray
        # - TO keep track, we can use a running bitmask which starts from 0. We AND any new number and check if its 0, then all good.
        longest = 0
        win_start = 0
        bitmask = 0
        for win_end, num in enumerate(nums):
            
            while (bitmask & num) != 0:
                bitmask &= ~nums[win_start]
                win_start += 1

            bitmask |= num
            longest = max(longest, (win_end - win_start) + 1)

        return longest
