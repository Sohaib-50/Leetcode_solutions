class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)

        left_prefixes = [0] * l
        for i in range(1, l):
            left_prefixes[i] = left_prefixes[i - 1] + nums[i - 1]

        right_prefixes = [0] * l
        for i in range(l - 2, -1, -1):
            print(i,end=', ')
            right_prefixes[i] = right_prefixes[i + 1] + nums[i + 1]

        for i in range(l):
            if left_prefixes[i] == right_prefixes[i]:
                return i
        
        return -1
