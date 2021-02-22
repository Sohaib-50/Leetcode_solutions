class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        frequencies = {}
        for index in range(len(nums)):
            if nums[index] in frequencies:
                frequencies[nums[index]] += 1
            else:
                frequencies[nums[index]] = 1
        
        count = 0
        for num in frequencies:
            frequency = frequencies[num]
            count += ((frequency ** 2) - frequency) //2
    
        return count