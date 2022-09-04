class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        # Bubble Sort Odd Indices
        nums = self.bubble_sort_alternate_indices(nums, start_index=1, reverse=True)
        
        # Bubble Sort Even Indices
        nums = self.bubble_sort_alternate_indices(nums, start_index=0, reverse=False)
        
        return nums
        
        
    def bubble_sort_alternate_indices(self, nums, start_index, reverse=False):
        swaps_needed = True
        while swaps_needed:
            i = start_index
            swaps_needed = False
            while (i + 2) < len(nums):
                if ((reverse) and (nums[i] < nums[i + 2])) or ((not reverse) and (nums[i] > nums[i + 2])):
                    nums[i], nums[i + 2] = nums[i + 2], nums[i]
                    swaps_needed = True
                i += 2
        return nums
            
                