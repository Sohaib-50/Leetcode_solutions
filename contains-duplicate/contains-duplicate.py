class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
            
        for i in counts:
            if counts[i] > 1:
                return True
        
        return False