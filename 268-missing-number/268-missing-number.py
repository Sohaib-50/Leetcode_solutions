class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        Intuition: Sum up all numbers in range [0, N].
        Then subtract all nums from nums from that sum, 
        remaining value will be the missing number.
        '''
        
        x = 0
        for i in range(len(nums) + 1):
            x += i
            
        for num in nums:
            x -= num

        return x
