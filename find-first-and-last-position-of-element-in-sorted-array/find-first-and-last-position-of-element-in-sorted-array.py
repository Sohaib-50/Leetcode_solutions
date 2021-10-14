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
                
        # linear search to find last occurance of target
        if ans[0] != -1:  # target exist in array
            current = ans[0]
            while (current < len(nums)) and (nums[current] == target):
                current += 1
            ans[1] = current - 1

        return ans
        