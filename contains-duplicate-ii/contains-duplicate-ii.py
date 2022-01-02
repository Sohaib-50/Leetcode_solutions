class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        prev_indices = {}
        for i, n in enumerate(nums):
            if n in prev_indices:
                idx_prev_n = prev_indices[n]
                if (idx_prev_n != i) and (abs(i - idx_prev_n) <= k):
                    return True
            prev_indices[n] = i
            
        return False