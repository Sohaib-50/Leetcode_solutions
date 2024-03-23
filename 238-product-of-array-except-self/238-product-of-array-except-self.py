class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_arr = nums.copy()
        for i in range(1, len(prefix_arr)):
            prefix_arr[i] = prefix_arr[i] * prefix_arr[i - 1]
        # print(prefix_arr)

        suffix_arr = nums.copy()
        for i in range(len(suffix_arr) - 2, -1, -1):
            suffix_arr[i] = suffix_arr[i] * suffix_arr[i + 1]
        # print(suffix_arr)

        ans = []
        for i in range(len(nums)):
            current = 1
            if i != 0:
                current *= prefix_arr[i - 1]
            if i != len(nums) - 1:
                current *= suffix_arr[i + 1]
            ans.append(current)
        return ans
