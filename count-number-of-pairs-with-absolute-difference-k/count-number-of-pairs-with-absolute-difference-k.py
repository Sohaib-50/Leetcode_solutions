class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
#         set count to 0
#         pick a number from nums
#             start picking every number from next position
#                 subtraact both nums, calculate abs
#                 if ans == k then increment count
                
#         return the count   
        count = 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count