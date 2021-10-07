class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            idx_to_mark = abs(i) - 1
            if nums[idx_to_mark] < 0:  # negative, i.e. already visited
                ans.append(abs(i))
            else:
                nums[idx_to_mark] *= -1
        
        return ans