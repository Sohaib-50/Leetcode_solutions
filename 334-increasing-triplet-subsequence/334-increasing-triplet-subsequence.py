class Solution:

    def increasingTriplet(self, nums: List[int]) -> bool:
        ''' Aproach 1, greedy '''
        earliest_min = second_earliest_min = float('inf')
        
        for num in nums:
            if num > second_earliest_min:
                return True

            else:
                if num < earliest_min:
                    earliest_min = num
                elif num < second_earliest_min and num > earliest_min:
                    second_earliest_min = num

        return False





    # def increasingTriplet(self, nums: List[int]) -> bool:
    #     ''' Aproach 0, brute force '''
    #     for i in range(len(nums) - 2):
    #         n1 = nums[i]
    #         for j in range(i + 1, len(nums) - 1):
    #             n2 = nums[j]
    #             if n1 >= n2:
    #                 continue
    #             for k in range(j + 1, len(nums)):
    #                 n3 = nums[k]
    #                 if n1 < n2 < n3:
    #                     return True
    #     return False
