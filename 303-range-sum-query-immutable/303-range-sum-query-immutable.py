class NumArray:

    def __init__(self, nums: List[int]):
        self.cumulative_sum = [0]
        current_sum = 0
        for i in nums:
            current_sum += i
            self.cumulative_sum.append(current_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.cumulative_sum[right + 1] - self.cumulative_sum[left]

# [-2,0,3,-5,2,-1]
# [0 -2, -2, 1, -4, -2, -3]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)