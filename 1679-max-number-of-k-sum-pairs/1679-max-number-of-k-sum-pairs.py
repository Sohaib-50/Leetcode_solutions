class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        ops = 0
        while l < r:
            sum_ = nums[l] + nums[r]
            if sum_ == k:
                l += 1
                r -= 1
                ops += 1
            elif sum_ < k:
                l += 1
            else:
                r -= 1

        return ops
