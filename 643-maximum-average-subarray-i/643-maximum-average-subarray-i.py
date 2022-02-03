class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        window_sum = 0
        max_avg = float("-inf")
        for end in range(len(nums)):
            window_sum += nums[end]
            if start + (k - 1) == end:
                max_avg = max(max_avg, window_sum / k)
                window_sum -= nums[start]
                start += 1
                
        return max_avg
                