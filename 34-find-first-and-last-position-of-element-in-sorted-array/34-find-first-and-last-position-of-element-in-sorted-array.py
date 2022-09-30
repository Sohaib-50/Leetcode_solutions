class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        while low <= high and nums[mid] != target:
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2
            
        if low > high:
            return [-1, -1]
        
        answer = []
        
        # find first position
        current = mid
        while current >= 0 and nums[current] == target:
            current -= 1
        answer.append(current + 1)
        
        # find last position
        current = mid
        while current < len(nums) and nums[current] == target:
            current += 1
        answer.append(current - 1)
        
        return answer
        
        
        