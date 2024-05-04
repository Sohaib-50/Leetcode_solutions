class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_start = 0
        window_sum = 0
        max_avg = float('-inf')
        for window_end in range(len(nums)):

            window_sum += nums[window_end]

            if window_end - window_start + 1 == k:
                max_avg = max(max_avg, window_sum / k)
                window_sum -= nums[window_start]
                window_start += 1
                
        return max_avg
