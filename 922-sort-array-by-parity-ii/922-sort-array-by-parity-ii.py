class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_nums = [i for i in nums if i % 2 == 0]
        odd_nums = [i for i in nums if i % 2 == 1]
        
        i = 0
        for num in even_nums:
            nums[i] = num
            i += 2
            
        i = 1
        for num in odd_nums:
            nums[i] = num
            i += 2
            
        return nums