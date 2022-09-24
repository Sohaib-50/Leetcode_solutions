class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counter = {}
        for arr in nums:
            for n in arr:
                counter[n] = counter.get(n, 0) + 1
        
        ans = []
        for n in counter:
            if counter[n] == len(nums):
                ans.append(n)
                
        return sorted(ans)