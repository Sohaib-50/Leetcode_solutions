class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        occurances = {}
        
        for i in nums:
            occurances[i] = occurances.get(i, 0) + 1
        
        duplicate = missing = 0
        for i in range(1, len(nums) + 1):
            if not occurances.get(i):
                missing = i
            elif occurances[i] == 2:
                duplicate = i
                
            if duplicate and missing:
                return duplicate, missing