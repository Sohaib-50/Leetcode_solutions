class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count_evens = 0
        
        for num in nums:
            count_num_digits = 0
            while num != 0:
                num //= 10
                count_num_digits += 1
            if count_num_digits % 2 == 0:
                count_evens += 1
                
        return count_evens