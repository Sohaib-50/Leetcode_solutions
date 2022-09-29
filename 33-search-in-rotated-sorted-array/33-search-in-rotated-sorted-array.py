class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if (nums[mid] == target):
                return mid
            
            else:
                if ((target < nums[0]) == (nums[mid] < nums[0])):
                    current = nums[mid]
                elif (nums[mid] < nums[0]):
                    current = float('inf')
                else:
                    current = float('-inf')
                    
                
                if current > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            
            
        return -1