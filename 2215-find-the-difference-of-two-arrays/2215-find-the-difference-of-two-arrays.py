class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [set(), set()]
        set1 = set(nums1)
        set2 = set(nums2)
        
        for num in nums1:
            if num not in set2:
                ans[0].add(num)

        for num in nums2:
            if num not in set1:
                ans[1].add(num)
        
        return ans
