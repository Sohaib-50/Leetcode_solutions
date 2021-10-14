class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search to find first occurance of target
        nums_len = len(nums)
        low = 0
        high = nums_len - 1
        
        ans = [-1, -1]
        
        while (low <= high) and (ans[0] == -1):
            mid = (high + low) // 2
            if (nums[mid] == target):
                if mid == 0 or nums[mid - 1] != target:  # if at first occurance of target
                    ans[0] = mid
                else:
                    high = mid - 1
            elif nums[mid] < target:
                low = mid + 1  # disregard left half of array
            else:
                high = mid - 1
                
        # binary search to find last occurance of target
        if ans[0] != -1:  # target exist in array
            low = ans[0]
            high = nums_len - 1
            while (ans[1] == -1):
                mid = (high + low) // 2
                if nums[mid] == target:
                    if ((mid == nums_len - 1) or (nums[mid + 1] != target)): # at last occurance of target
                        ans[1] = mid
                    else:
                        low = mid + 1
                    
                else:  # answer must be in left half
                    high = mid - 1
                    
        return ans
        