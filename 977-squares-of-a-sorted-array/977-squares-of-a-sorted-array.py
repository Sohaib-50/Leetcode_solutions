class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in nums]
        right = len(nums) - 1
        left = 0
        
        for i in range(len(nums) - 1, -1, -1):
            left_num = nums[left]
            right_num = nums[right]
            
            if abs(left_num) > abs(right_num):
                ans[i] = left_num ** 2
                left += 1
                
            else:
                ans[i] = right_num ** 2
                right -= 1
        
        return ans