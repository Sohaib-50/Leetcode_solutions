class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        answer = 0
        lookup = set(nums)
        
        for i, n in enumerate(nums):
            if ((n + diff) in lookup) and ((n + (2 * diff)) in lookup):
                answer += 1
        
        return answer