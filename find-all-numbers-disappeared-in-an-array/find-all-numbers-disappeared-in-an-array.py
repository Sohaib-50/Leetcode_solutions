class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_counter = {}
        ans = []
        for i in range(1, len(nums) + 1):
            nums_counter[i] = 0
        
        for i in nums:
            nums_counter[i] += 1
        
        for i in nums_counter:
            if nums_counter[i] == 0:
                ans.append(i)
                
        return ans