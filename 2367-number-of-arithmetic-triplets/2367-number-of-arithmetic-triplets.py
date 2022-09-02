class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        answer = 0
        lookup = {}
        for i in range(len(nums)):
            lookup[nums[i]] = i
        
        for i, n in enumerate(nums):
            if lookup.get(n + diff) and lookup.get(n + (2 * diff)):
                answer += 1
        
        return answer