class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ### IDEA: reverse sorting, start placing largest elements to end of nums1
        
        # pointers to last of n1 and n2
        nums1_ptr = m - 1
        nums2_ptr = n - 1
    
        i = m + n - 1  # current position to add to in nums1
        while (nums1_ptr >= 0) and (nums2_ptr >= 0):  # till elements remain in BOTH nums1 and nums2
            if nums1[nums1_ptr] > nums2[nums2_ptr]:
                nums1[i] = nums1[nums1_ptr]
                nums1_ptr -= 1
            else:
                nums1[i] = nums2[nums2_ptr]
                nums2_ptr -= 1
            i -= 1
        
        # add remaining items
        if nums1_ptr < 0:
            for j in range(nums2_ptr, -1, -1):
                nums1[i] = nums2[j]
                i -= 1
        else:
            for j in range(nums1_ptr, -1, -1):
                nums1[i] = nums1[j]
                i -= 1
            