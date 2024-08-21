class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # help: https://leetcode.com/problems/sum-of-distances/solutions/3395726/explained-with-images-easy-to-understand
        
        arr = [0 for _ in nums]
        nums_indices = {}
        
        for i, num in enumerate(nums):
            if num not in nums_indices:
                nums_indices[num] = []
            nums_indices[num].append(i)

        for num in nums_indices:
            indices = nums_indices[num]
            pre_sum = 0
            post_sum = sum(indices)

            for i, index in enumerate(indices):

                post_sum -= index

                # left side calculations (index - j for all j towards the left (smaller than index))
                arr[index] += index * i  # add index for however many indices are on the left times
                arr[index] -= pre_sum  # subtract off each of the indices on the left 

                # right side calculations (j - index for all j towards the right (larger than index))
                arr[index] -= index * (len(indices) - i - 1)  # subtract off the index however many indices are on the right times
                arr[index] += post_sum  # add each of the indices on the right

                pre_sum += index

        return arr
