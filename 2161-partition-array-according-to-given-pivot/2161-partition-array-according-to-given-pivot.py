class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [pivot for i in nums]
        less_than_ptr = 0
        more_than_ptr = len(ans) - 1
        
        for i in range(len(nums)):
            if nums[i] < pivot:
                ans[less_than_ptr], less_than_ptr = nums[i], less_than_ptr + 1
            if nums[~i] > pivot:
                ans[more_than_ptr], more_than_ptr = nums[~i], more_than_ptr - 1
                
        return ans