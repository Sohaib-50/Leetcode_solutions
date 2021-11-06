class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        frequencies = {};
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1;
            
        ans = []
        for num in frequencies:
            if frequencies.get(num) == 1:
                ans.append(num)
        
        return ans