class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        longest = 0
        
        for end in range(len(nums)):
            if nums[end] == 0:

                # can flip
                if k > 0:
                    k -= 1

                # can't flip
                else:
                    # shrink window
                    while nums[start] != 0:
                        start += 1
                    start += 1
                    
            longest = max(longest, end - start + 1)
        
        return longest
