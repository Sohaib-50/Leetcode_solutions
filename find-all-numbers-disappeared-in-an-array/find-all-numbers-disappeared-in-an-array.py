class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # mark every index i for which i + 1 exists in nums
        for i in range(len(nums)):
            index_to_mark = abs(nums[i]) - 1
            nums[index_to_mark] = abs(nums[index_to_mark]) * -1
        
        # find out all indexes for which the number at the index is positive
        # that means  (index + 1) doesnt exist in the array nums 
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:  # positive
                ans.append(i + 1)
        
        return ans